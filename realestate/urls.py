from django.conf.urls import patterns, url

from . import views


prefix = "re-"

urlpatterns = patterns('',
    url(r'^(?P<slug>\S+)/properties/$', views.company_properties, 
        name=prefix + "company-properties"),
    url(r'^(?P<slug>\S+)/members/$', views.company_members, 
        name=prefix + "company-members"),
    url(r'^(?P<slug>\S+)/support/$', views.company_support, 
        name=prefix + "company-support"),
    url(r'^(?P<slug>\S+)/$', views.company_home, name=prefix + "company-home"),

    url(r'^$', views.home, name=prefix + "home"),
)