from django.conf.urls import patterns, url

from scrape import views


urlpatterns = patterns('',
    url(r'^data/$', views.apartment_list_data , name="scrape-data"),
)