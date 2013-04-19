from google.appengine.ext import db
from google.appengine.api import memcache
import logging

class Player(db.Model):
  """A class representing a player."""

  # Constants
  INITIAL_ELO = 1500.0
  SENSATIVITY_FACTOR = 400.0

  # Reference to the account of player
  account = db.ReferenceProperty(required=True, collection_name='__account_player_set')
  # Reference to the pool the player is in
  pool = db.ReferenceProperty(required=True)
  # eloRating for the player
  __eloRating = db.FloatProperty(default=INITIAL_ELO)
  # username used to identify the player
  username = db.StringProperty(required=True)
  # List of keys for all the games a player has played in
  __gameKeys = db.ListProperty(item_type=db.Key,default=[])

  @classmethod
  def createPlayer(cls, account, username, pool):
    """ Simple method for creating players. """
    player = cls(pool=pool,username=username, account= account, parent=account)
    player.put()
    pool.addPlayer(player)
    pool.put()
    return player


  def getProbabilityOfVictory(self,otherPlayer):
    """ This function calculates and returns the predicted probability that 
    the current player wins against the player provided as an argument. The 
    probability the other player wins can be found be 1 - this value."""
    denominator = (1 + pow(10,(otherPlayer.eloRating-self.eloRating)/self.SENSATIVITY_FACTOR))
    expectedWinProbSelf = 1.0/ denominator
    return expectedWinProbSelf

  def getGames(self):
    """ Gets all the Game objects for a Player."""
    gamesList = []
    for key in self.__gameKeys:
      game = db.get(key)
      gamesList.append(game)
    return gamesList

  def updateEloRating(self, newElo):
    """ Updates the elo rating for a Player. """
    self.__eloRating = newElo
    self.put()

  def getEloRating(self):
    return self.__eloRating

  def addGame(self,game):
    self.__gameKeys.append(game.key())
    self.put()

class Team(db.Model):
  """A class representing a team"""

  # CONSTANTS
  SENSATIVITY_FACTOR = 400.0

  # PRIVATE INSTANCE VARIABLES
  # List of keys for the players on the team
  __playerKeys = db.ListProperty(item_type=db.Key,default=[])
  # This instance variable caches the team's elo, intialized to None
  __teamELO = None

  # PUBLIC INSTANCE VARIABLES
  # A description of the team, could be a name
  description = db.StringProperty()

  @classmethod
  def createTeamWithPlayers(cls, players, description=None):
    """ This method creates a new team with the supplied players. """
    playerKeyList = []
    # Add all the players to the playerKey list
    for player in players:
      key = player.key()
      playerKeyList.append(key)
    team = cls(__playerKeys=playerKeyList)
    team.description = description
    team.put()
    return team

  def getPlayers(self):
    """ Gets all the Player objects for a Team."""
    playerList = []
    for key in self.__playerKeys:
      player = db.get(key)
      playerList.append(player)
    return playerList

  def getTeamELO(self):
    """ Returns the summed total of all the players' elos. """
    if self.__teamELO is None:
      teamELO = 0
      teamPlayers = self.getPlayers()
      for player in teamPlayers:
        teamELO = teamELO + player.eloRating
      self.__teamELO = teamELO
    return self.__teamELO

  def getProbabilityOfVictory(self,otherTeam):
    teamELO = self.getTeamELO()
    otherTeamELO = otherTeam.getTeamELO()

    # Calculate chance of team winning versus otherTeam
    denominator = (1 + pow(10,(otherTeamELO-teamELO)/self.SENSATIVITY_FACTOR))
    chanceOfWinning = 1.0/ denominator
    return chanceOfWinning

  def updateTeamELO(self, newELO):
    eloDifference = newELO - self.getTeamELO()
    for player in self.getPlayers():
      eloProportion = float(player.eloRating)/ self.getTeamELO()
      proportionedEloForPlayer = eloProportion * eloDifference
      player.updateEloRating(player.getEloRating() + proportionedEloForPlayer)
    self.__teamELO = newELO

  def addGame(self,game):
    for player in self.getPlayers():
      player.addGame(game)

class Pool(db.Model):
  """A class representing a pool of players competeting against each other."""

  # PRIVATE INSTANCE VARIABLES
  __adminKeys = db.ListProperty(item_type=db.Key,default=[])
  __playerKeys = db.ListProperty(item_type=db.Key,default=[])

  # PUBLIC INSTANCE VARIABLES
  poolName = db.StringProperty()
  description = db.StringProperty()

  def getPlayers(self):
    playerList = []
    for key in self.__playerKeys:
      player = db.get(key)
      playerList.append(player)
    return playerList

  def addPlayer(self,player):
    self.__playerKeys.append(player.key())
    self.put()

  def getAdmins(self):
    adminsList = []
    for key in self.__adminKeys:
      admin = db.get(key)
      adminsList.append(admin)
    return adminsList

  def addAdmin(self,player):
    self.__adminKeys.append(player.key())
    self.put()

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
      team.addGame(game)
    return game

  def __calculateNewElos(self):
    newElos = []
    teams = self.getTeams()
    curTeamIndex = 0
    while curTeamIndex < len(teams):
      curTeam = teams[curTeamIndex]
      expectedWins = 0
      # Calculate expected number of wins
      for otherTeam in teams:
        if otherTeam!=curTeam:
          expectedWins = expectedWins + curTeam.getProbabilityOfVictory(otherTeam)
      # Calculate actual number of wins (simply based on position in list)
      actualWins = (len(teams)-1)-curTeamIndex
      curTeamIndex = curTeamIndex +1
      newELO = curTeam.getTeamELO() + self.K_FACTOR * (actualWins - expectedWins)
      newElos.append(newELO)
    return newElos

  def __updateRatingsForEachPlayer(self, newRatings):
    teams = self.getTeams()
    curTeamIndex = 0
    while (curTeamIndex < len(teams)):
      # Get player and update eloRating
      curTeam = teams[curTeamIndex]
      newRatingForCurrentTeam = newRatings[curTeamIndex]
      curTeam.updateTeamELO(newRatingForCurrentTeam)
      # Update while loop index
      curTeamIndex = curTeamIndex+1

  def updateRatings(self):
    newRatings = self.__calculateNewElos()
    self.__updateRatingsForEachPlayer(newRatings)

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
