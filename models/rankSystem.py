from google.appengine.ext import db
from google.appengine.api import memcache
import logging

class Player(db.Model):
  """A class representing a player."""

  INITIAL_ELO = 1500.0
  SENSATIVITY_FACTOR = 400.0

  # Reference to the account of player
  account = db.ReferenceProperty(required=True, collection_name='account_player_set')
  # Reference to the pool the player is in
  pool = db.ReferenceProperty(required=True)
  eloRating = db.FloatProperty(default=INITIAL_ELO)
  username = db.StringProperty(required=True)
  #List of keys for all the games a player has played in
  gameKeys = db.ListProperty(item_type=db.Key,default=[])

  def probabilityOfWinning(self,otherPlayer):
    """ This function calculates and returns the predicted probability that 
    the current player wins against the player provided as an argument. The 
    probability the other player wins can be found be 1 - this value."""
    denominator = (1 + pow(10,(otherPlayer.eloRating-self.eloRating)/self.SENSATIVITY_FACTOR))
    expectedWinProbSelf = 1.0/ denominator
    return expectedWinProbSelf

  def getGames(self):
    """ Gets all the Game objects for a Player."""
    gamesList = []
    for key in self.gameKeys:
      game = db.get(key)
      gamesList.append(game)
    return gamesList

  def updateEloRating(self, newElo):
    """ Updates the elo rating for a Player. """
    self.eloRating = newElo
    logging.info("New Elo: " + str(newElo))
    self.put()

  def getEloRating(self):
    return self.eloRating

  def addPlayerToGame(self,game):
    self.gameKeys.append(game.key())
    self.put()

class Team(db.Model):
  """A class representing a team"""

  #Constants
  SENSATIVITY_FACTOR = 400.0

  playerKeys = db.ListProperty(item_type=db.Key,default=[])
  description = db.StringProperty()
  # Initialize teamELO to zero
  __teamELO = None

  @classmethod
  def createTeamWithPlayers(cls, players, description=None):
    """ This method creates a new team with the given players. """
    playerKeyList = []
    for player in players:
      key = player.key()
      playerKeyList.append(key)
    team = cls(playerKeys=playerKeyList)
    team.description = description
    team.put()
    return team

  def getPlayers(self):
    """Gets all the Player objects for a Team."""
    playerList = []
    for key in self.playerKeys:
      player = db.get(key)
      playerList.append(player)
    return playerList

  def getTeamELO(self):
    if self.__teamELO is None:
      teamELO = 0
      teamPlayers = self.getPlayers()
      for player in teamPlayers:
        teamELO = teamELO + player.eloRating
      self.__teamELO = teamELO
    return self.__teamELO

  def probabilityOfWinning(self,otherTeam):
    teamELO = self.getTeamELO()
    otherTeamELO = otherTeam.getTeamELO()

    # Calculate chance of team winning versus otherTeam
    denominator = (1 + pow(10,(otherTeamELO-teamELO)/self.SENSATIVITY_FACTOR))
    chanceOfWinning = 1.0/ denominator
    return chanceOfWinning

  def updateTeamELO(self, newELO):
    eloDifference = newELO - self.getTeamELO()
    logging.info("Elo Difference: " + str(eloDifference))
    for player in self.getPlayers():
      eloProportion = float(player.eloRating)/ self.getTeamELO()
      proportionedEloForPlayer = eloProportion * eloDifference
      player.updateEloRating(player.getEloRating() + proportionedEloForPlayer)

  def addPlayersToGame(self,game):
    for player in self.getPlayers():
      player.addPlayerToGame(game)

class Pool(db.Model):
  """A class representing a pool of players competeting against each other."""

  adminKeys = db.ListProperty(item_type=db.Key,default=[])
  playerKeys = db.ListProperty(item_type=db.Key,default=[])

  def getPlayers(self):
    playerList = []
    for key in self.playerKeys:
      player = db.get(key)
      playerList.append(player)
    return playerList

  def getAdmins(self):
    adminsList = []
    for key in self.adminKeys:
      admin = db.get(key)
      adminsList.append(admin)
    return adminsList

class Game(db.Model):
  """A game representing the results of a risk game"""

  # K_FACTOR could become elo dependent eventually
  K_FACTOR = 32

  #List of keys for all the teams in the game
  teamKeys = db.ListProperty(item_type=db.Key,default=[])
  date = db.DateTimeProperty(auto_now_add=True)

  @classmethod
  def createGameWithTeams(cls, teams):
    """ This method creates a new game with the given teams. The order of the 
    teams represents the order of their finishes. """
    teamKeyList = []
    for team in teams:
      key = team.key()
      teamKeyList.append(key)
    game = cls(teamKeys=teamKeyList)
    game.put()
    for team in teams:
      team.addPlayersToGame(game)
    return game

  

  def calculateNewELOs(self):
    curTeamIndex = 0
    newELOs = []
    teams = self.getTeams()
    logging.info(len(teams))
    while curTeamIndex < len(teams):
      curTeam = teams[curTeamIndex]
      expectedWins = 0
      # Calculate expected number of wins
      for otherTeam in teams:
        if otherTeam!=curTeam:
          expectedWins = expectedWins + curTeam.probabilityOfWinning(otherTeam)
      # Calculate actual number of wins (simply based on position in list)
      actualWins = (len(teams)-1)-curTeamIndex
      curTeamIndex = curTeamIndex +1
      newELO = curTeam.getTeamELO() + self.K_FACTOR * (actualWins - expectedWins)
      newELOs.append(newELO)
    curTeamIndex = 0
    while (curTeamIndex < len(teams)):
      # Get player and update eloRating
      curTeam = teams[curTeamIndex]
      logging.info("Cur Team: " + curTeam.description + "Elo: " + str(newELOs[curTeamIndex]))
      newELOForCurTeam = newELOs[curTeamIndex]
      curTeam.updateTeamELO(newELOForCurTeam)
      # Update while loop index
      curTeamIndex = curTeamIndex+1

  def getTeams(self):
    """ Gets all the player objects for a Game."""
    teamList = []
    for key in self.teamKeys:
      team = db.get(key)
      teamList.append(team)
    return teamList

class Account(db.Model):
  """ Represents an account.  One account can have many players in different pools."""
  facebookID = db.StringProperty()
  firstName = db.StringProperty()
  lastName = db.StringProperty()
