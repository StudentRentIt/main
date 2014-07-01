from django.conf.urls import patterns, url

from scrape import views


urlpatterns = patterns('',
    url(r'^admin/(?P<city>\d+)/$', views.admin, name="scrape-city"),
    url(r'^admin/$', views.admin, name="scrape-admin"),
    url(r'^add/(?P<pk>\d+)/$', views.add_property, name="scrape-add"),
    url(r'^history/$', views.history, name="scrape-history"),
)