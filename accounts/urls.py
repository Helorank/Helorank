from accounts import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^dashboard/$', views.dashboard, name='dashboard'),
  url(r'^signup/$', views.signup, name='signup'),
)