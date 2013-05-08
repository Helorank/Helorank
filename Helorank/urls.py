from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from Helorank.settings import DEBUG
admin.autodiscover()
from Helorank import views

urlpatterns = patterns('',
  # Examples:
  url(r'^$', views.index, name="index"),
  url(r'^login/$', views.login, name="login"),
  url(r'^logout/$', views.logout, name="logout"),
  url(r'^signUp/$', views.signUp, name="signUp"),
  url(r'^welcome/$',views.welcome, name="welcome"),
  url(r'^account/', include('accounts.urls', namespace="accounts")),
  url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    #urlpatterns += patterns('',
    #    (r'^static/(?P<path>.*)', 'django.views.static.serve', {
    #    'document_root': settings.STATIC_URL}
    #))
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_URL)