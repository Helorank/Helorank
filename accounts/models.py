from django.db import models

# Create your models here.
class Account(models.Model):
  email = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  creation_date = models.DateTimeField('date created')
  facebook_ID = models.CharField(max_length=200)
  twitter_ID = models.CharField(max_length=200)
  age = models.IntegerField(default=0)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.email

  def get_full_name(self):
    return self.first_name + " " + self.last_name
