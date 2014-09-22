from django.conf.urls import patterns, url

from school import views

app_prefix = 'school-'

urlpatterns = patterns('',
    url(r'^$', views.home, name=app_prefix + 'home'),
)