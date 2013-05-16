from django.db import models
from accounts.models import Account
from leagues.settings import SENSATIVITY_FACTOR, SENSATIVITY_BASE

class League(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)

  admin_accounts = models.ManyToManyField(Account)

  def __unicode__(self):
    return self.name + " #" + str(self.id)

class Player(models.Model):
  account = models.ForeignKey(Account)
  rating = models.IntegerField()
  league = models.ForeignKey(League)

  def get_prob_of_winning(self,other_player):
    """ This function calculates and returns the predicted probability that
    the current player wins against the player provided as an argument. The
    probability the other player wins can be found be 1 - this value."""
    denominator = (1 + pow(SENSATIVITY_BASE,(other_player.rating-self.rating)/SENSATIVITY_FACTOR))
    expected_win_prob = 1.0/ denominator
    return expected_win_prob

  def __unicode__(self):
    return self.account.email + ": " + self.account.username + " Rating: " + str(self.rating)

class Game(models.Model):
  players = models.ManyToManyField(Player)
  league = models.ForeignKey(League)
  date_created = models.DateTimeField('date created', auto_now_add=True)
  has_been_submitted = models.BooleanField(default=False)
 
  class Team():
    """A non-persistant Team object, used to simplify submitting game.

    Keyword Arguments For Initializer:
    players -- A list of Player objects who are on the team.

    """
    def __init__(self, players):
      self.players = players

    def get_team_rating(self):
      # Attempt to find cached team rating, otherwise calculate it
      if self.team_rating is None:
        team_rating = 0
        for player in self.players:
          team_rating += player.rating
        self.team_rating = team_rating
      return self.team_rating

    def get_prob_of_winning(self,other_team):
      self_rating = self.get_team_rating()
      other_rating = other_team.get_team_rating()

      denominator = (1 + pow(SENSATIVITY_BASE,(other_rating-self_rating)/SENSATIVITY_FACTOR))
      expected_win_prob = 1.0/ denominator
      return expected_win_prob

    def update_team_rating(self, new_rating):
      rating_difference = new_rating - self.get_team_rating()
      for player in self.players:
        rating_proportion = float(player.rating)/self.get_team_rating()
        rating_proportioned_for_player = rating_difference * rating_proportion
        player.rating += rating_proportioned_for_player
        player.save()
      # Update team_rating cache
      self.team_rating = new_rating

  def determine_teams(self):
    """ Returns a list of the Teams for the game. """
    rank_list = self.ranks
    


  def submit_game(self):
    """ Called after ranks have been saved. """
    team_list = determine_teams(ranks)

  def __unicode__(self):
    player_strings = [unicode(player) for player in self.players.all()]
    return " ".join(player_strings) + " " + str(self.date_created)


class Rank(models.Model):
  game = models.ForeignKey(Game)
  player = models.ForeignKey(Player)
  rank_index = models.IntegerField()

  def __unicode__(self):
    return unicode(player) + ", Rank: " + str(rank_index) + " Game: " + unicode(game)
