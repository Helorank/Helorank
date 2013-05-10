from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from Helorank import views
from Helorank.settings import DEBUG
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', views.under_construction, name='index'),
  url(r'^account/', include('accounts.urls', namespace='accounts')),
  url(r'^admin/', include(admin.site.urls), name='admin'),
  url(r'^login/$', views.login, name='login'),
  url(r'^logout/$', views.logout, name='logout'),
)

if settings.DEBUG:
  # static files (images, css, javascript, etc.)
  #urlpatterns += patterns('',
  #    (r'^static/(?P<path>.*)', 'django.views.static.serve', {
  #    'document_root': settings.STATIC_URL}
  #))
  urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_URL)