from django.conf.urls import patterns, url

from report import views

prefix = 'report-'

urlpatterns = patterns('',
    url(r'^admin/$', views.admin_home, name=prefix + 'admin-home'),
    url(r'^realestate/$', views.real_estate_home, name=prefix + 'real-estate-home'),
    url(r'^business/$', views.business_home, name=prefix + 'business-home'),
)