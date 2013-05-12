from accounts import views
from django.conf.urls import patterns, url
import Helorank

urlpatterns = patterns('',
  url(r'^dashboard/$', Helorank.views.requires_login(views.dashboard), name='dashboard'),
  url(r'^signup/$', views.signup, name='signup'),
)