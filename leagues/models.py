from django.db import models
from accounts.models import Account

# Create your models here.
class League(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)

  admin_accounts = models.ManyToManyField(Account)

class Player(models.Model):
  name = models.CharField(max_length=200)
  account = models.ForeignKey(Account)
  rating = models.IntegerField()
  league = models.ForeignKey(League)