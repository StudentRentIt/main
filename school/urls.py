from django.conf.urls import patterns, url

from school import views

prefix = 'school-'

urlpatterns = patterns('',
    url(r'^$', views.home, name=prefix + 'home'),
    url(r'^(?P<slug>\S+)/(?P<type>neighborhood)/(?P<n_slug>\S+)/$', views.school_info,
        name=prefix + "neighborhood"),
    url(r'^(?P<slug>\S+)/(?P<type>info)/$', views.school_info, name=prefix + 'info'),
)