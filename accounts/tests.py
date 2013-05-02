from django.test import TestCase

from accounts.models import Account

class AccountMethodTest(TestCase):

  def setUp(self):
    self.account = Account(email="test@test.com",username="Tester1",password="ZZTop")
    self.account.first_name = "Cody"
    self.account.last_name = "Sam"

  def test_get_full_name(self):
    self.assertEqual(self.account.get_full_name(), "Cody Sam")