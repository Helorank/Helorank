from django.db import models

# Create your models here.
class Account(models.Model):
  email = models.EmailField(verbose_name='e-mail')
  password = models.CharField(max_length=200)
  creation_date = models.DateTimeField('date created', auto_now_add=True)
  facebook_ID = models.CharField(max_length=200, blank=True)
  twitter_ID = models.CharField(max_length=200, blank=True)
  age = models.IntegerField(null=True)
  username = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200, blank=True)
  last_name = models.CharField(max_length=200, blank=True)
  gravatar_hash = models.CharField(max_length=200, blank=True)
  influence = models.IntegerField(null=True, blank=True)
#  leagues = models.ManyToManyField(League)
#  friends = models.ManyToManyField(Account)

  def __unicode__(self):
    return self.email

  class Meta:
    ordering = ['email']

  def get_full_name(self):
    return u'%s %s' % (self.first_name, self.last_name)

# class Player(models.Model)
#  account = models.ForeignKey(Account)