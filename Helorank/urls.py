from django.conf.urls import patterns, include, url

from django.contrib import admin
from Helorank.settings import DEBUG
admin.autodiscover()
from Helorank import views

urlpatterns = patterns('',
  # Examples:
  url(r'^$', views.index, name="index"),
  url(r'^welcome/',views.welcome, name="welcome"),
  url(r'^admin/', include(admin.site.urls)),
)
