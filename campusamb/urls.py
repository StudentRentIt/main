from django.conf.urls import patterns, url

from campusamb import views

app_prefix = 'ca-'

urlpatterns = patterns('',
    # top level app urls
    url(r'^$', views.home, name=app_prefix + 'home'),
    url(r'^dashboard/$', views.dashboard, name=app_prefix + 'dashboard'),
    url(r'^support/$', views.support, name=app_prefix + 'support'),

    # property subapp urls
    url(r'^property/add/$', views.add_property, name=app_prefix + 'add-property'),
    url(r'^property/manage/$', views.manage_property, name=app_prefix + 'manage-property'),
    url(r'^property/edit/(?P<pk>\d+)/$', views.edit_property,
        name=app_prefix + 'edit-property'),

    # content subapp urls
    url(r'^content/(?P<type>\S+)/add/$', views.add_content, name=app_prefix + 'add-content'),
    url(r'^content/(?P<type>\S+)/(?P<pk>\d+)/$', views.edit_content,
        name=app_prefix + 'edit-content'),
    url(r'^content/manage/$', views.manage_content, name=app_prefix + 'manage-content'),
    url(r'^content/edit/$', views.edit_content, name=app_prefix + 'edit-content'),
)