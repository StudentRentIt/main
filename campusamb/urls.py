from django.conf.urls import patterns, url

from campusamb import views

app_prefix = 'ca-'

urlpatterns = patterns('',
    url(r'^$', views.home, name=app_prefix + 'home'),
    url(r'^dashboard/$', views.dashboard, name=app_prefix + 'dashboard'),
    url(r'^support/$', views.support, name=app_prefix + 'support'),

    url(r'^property/add/$', views.add_property, name=app_prefix + 'add-property'),
    url(r'^property/edit/$', views.edit_property, name=app_prefix + 'edit-property'),

    url(r'^content/add/$', views.add_content, name=app_prefix + 'add-content'),
    url(r'^content/edit/$', views.edit_content, name=app_prefix + 'edit-content'),
)