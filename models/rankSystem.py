from google.appengine.ext import db
from google.appengine.api import memcache

class Player(db.Model):
  """A class representing a player"""

  INITIAL_ELO = 1500.0
  SENSATIVITY_FACTOR = 400.0

  eloRating = db.FloatProperty(default=INITIAL_ELO)
  firstName = db.StringProperty()
  lastName = db.StringProperty()

  def probabilityOfWinning(self,otherPlayer):
    """ This function calculates and returns the predicted probability that the current player wins against the player provided as an argument. The probability the other player wins can be found be 1 - this value."""
    denominator = (1 + pow(10,(otherPlayer.eloRating-self.eloRating)/self.SENSATIVITY_FACTOR))
    expectedWinProbSelf = 1.0/ denominator
    return expectedWinProbSelf

class GameResult(db.Model):
  """A game representing the results of a risk game"""

  # K_FACTOR could become elo dependent eventually
  K_FACTOR = 32

  players = db.ListProperty(item_type=db.Key,default=[])
  date = db.DateTimeProperty(auto_now_add=True)

  def calculateNewELOs(self):
    curPlayerIndex = 0
    newELOs = []
    players = self.getPlayers()
    while curPlayerIndex < len(players):
      curPlayer = players[curPlayerIndex]
      expectedWins = 0
      # Calculate expected number of wins
      for otherPlayer in players:
        if otherPlayer!=curPlayer:
          expectedWins = expectedWins + curPlayer.probabilityOfWinning(otherPlayer)
      # Calculate actual number of wins (simply based on position in list)
      actualWins = (len(self.players)-1)-curPlayerIndex
      curPlayerIndex = curPlayerIndex +1
      newELO = curPlayer.eloRating + self.K_FACTOR * (actualWins - expectedWins)
      newELOs.append(newELO)
    curPlayerIndex = 0
    while (curPlayerIndex < len(players)):
      # Get player and update eloRating
      curPlayer = players[curPlayerIndex]
      newELOForCurPlayer = newELOs[curPlayerIndex]
      curPlayer.eloRating = newELOForCurPlayer
      curPlayer.put()
      # Update while loop index
      curPlayerIndex = curPlayerIndex+1

  def getPlayers(self):
    playersList = []
    for playerKey in self.players:
      player = db.get(playerKey)
      playersList.append(player)
    return playersList
