from django.db import models
from accounts.models import Account

class League(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)

  admin_accounts = models.ManyToManyField(Account)

  def __unicode__(self):
    return self.name + " #" + str(self.id)

class Player(models.Model):
  name = models.CharField(max_length=200)
  account = models.ForeignKey(Account)
  rating = models.IntegerField()
  league = models.ForeignKey(League)

  def get_prob_of_winning(self,other_player):
    """ This function calculates and returns the predicted probability that
    the current player wins against the player provided as an argument. The
    probability the other player wins can be found be 1 - this value."""
    denominator = (1 + pow(10,(other_player.rating-self.rating)/self.get_sensativity_factor()))
    expected_win_prob = 1.0/ denominator
    return expected_win_prob

  def get_sensativity_factor(self):
    return 400.0

  def __unicode__(self):
    return self.account.email + ": " + self.name + " Rating: " + str(self.rating)

class Game(models.Model):
  players = models.ManyToManyField(Player)
  league = models.ForeignKey(League)
  date_created = models.DateTimeField('date created', auto_now_add=True)

  def __unicode__(self):
    player_strings = [unicode(player) for player in self.players]
    return " ".join(player_strings) + " " + str(date_created)

class Rank(models.Model):
  game = models.ForeignKey(Game)
  player = models.ForeignKey(Player)
  rank = models.IntegerField()

  def __unicode__(self):
    return unicode(player) + ", Rank: " + str(rank) + " Game: " + unicode(game)
