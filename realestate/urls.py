from django.conf.urls import patterns, url

from realestate import views


urlpatterns = patterns('',
    url(r'^(?P<slug>\S+)/$', views.company, name="re-company"),
    url(r'^$', views.home, name="re-home"),
)