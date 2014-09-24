from django.conf.urls import patterns, url

from campusamb import views

app_prefix = 'ca-'

urlpatterns = patterns('',
    url(r'^$', views.home, name=app_prefix + 'home'),
    url(r'^dashboard/$', views.dashboard, name=app_prefix + 'dashboard'),
    url(r'^property/$', views.dashboard, name=app_prefix + 'property'),
    url(r'^content/$', views.dashboard, name=app_prefix + 'school-items'),
)