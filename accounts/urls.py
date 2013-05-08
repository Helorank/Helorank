from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('accounts.views',
  url(r'^createAccount/$', 'create_account_handler', name='detail'),
  url(r'^dashboard/$', 'dashboard', name='dashboard'),
  url(r'^profile/([^/]+)', 'profile')
)