from django.conf.urls import patterns, url

from school import views

app_prefix = 'school-'

urlpatterns = patterns('',
    url(r'^$', views.home, name=app_prefix + 'home'),

    url(r'^(?P<slug>\S+)/search/$', views.school_search, name=app_prefix + 'search'),
    url(r'^(?P<slug>\S+)/neighborhood/$', views.school_neighborhood, name="neighborhood"),

    url(r'^search/$', views.school_search, name="search"),
    url(r'^(?P<slug>\S+)/$', views.school_info, name=app_prefix + 'info'),
)