from django.db import models

# Create your models here.
class Account(models.Model):
  email = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  creation_date = models.DateTimeField('date created', auto_now_add=True)
  facebook_ID = models.CharField(max_length=200, blank=True)
  twitter_ID = models.CharField(max_length=200, blank=True)
  age = models.IntegerField(null=True)
  username = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200, blank=True)
  last_name = models.CharField(max_length=200, blank=True)
  profile_picture_url = models.URLField(max_length=200, blank=True)

  def __unicode__(self):
    return self.email

  def get_full_name(self):
    return self.first_name + " " + self.last_name
