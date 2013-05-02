from django.test import TestCase

from accounts.models import Account
from leagues.models import *

class LeagueMethodTests(TestCase):

  def setUp(self):
    self.account = Account(email="test@test.com",username="Tester1",password="ZZTop")
    self.account.first_name = "Cody"
    self.account.last_name = "Sam"
    self.league = League(name="TestLeague")
    self.league.save()

  def test_league_unicode_(self):
    self.assertEqual(unicode(self.league), "TestLeague #1")

class PlayerMethodTests(TestCase):

  def setUp(self):
    self.account = Account(email="test@test.com",username="Tester1",password="ZZTop")
    self.account.save()
    self.league = League(name="TestLeague")
    self.league.save()
    self.player1 = Player(account=self.account, rating=1500, name="KV35")
    self.player2 = Player(account=self.account, rating=1500, name="CS69")

  def test_player_unicode(self):
    self.assertEqual(unicode(self.player1),"test@test.com: KV35 Rating: 1500")

  def test_get_prob_of_winning(self):
    # Test if they have same rating
    self.assertEqual(self.player1.get_prob_of_winning(self.player2),0.5)

class GameMethodTests(TestCase):

  def setUp(self):
    self.account = Account(email="test@test.com",username="Tester1",password="ZZTop")
    self.player1 = Player(account=self.account, rating=1500, name="KV35")
    self.player2 = Player(account=self.account, rating=1450, name="CS69")

class RankMethodTests(TestCase):

  def setUp(self):
    self.account = Account(email="test@test.com",username="Tester1",password="ZZTop")
