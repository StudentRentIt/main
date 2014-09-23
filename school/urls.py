from django.conf.urls import patterns, url

from school import views

app_prefix = 'school-'

urlpatterns = patterns('',
    url(r'^$', views.home, name=app_prefix + 'home'),
    url(r'^search/$', views.school_search, name="search"),
    url(r'^(?P<slug>\S+)/(?P<type>neighborhood)/(?P<n_slug>\S+)/$', views.school_info,
        name=app_prefix + "neighborhood"),
    url(r'^(?P<slug>\S+)/(?P<type>info)/$', views.school_info, name=app_prefix + 'info'),
    url(r'^(?P<slug>\S+)/search/$', views.school_search, name=app_prefix + 'search'),
)