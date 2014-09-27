from django.conf.urls import patterns, url

from search import views

search_group_prefix = 'search-group-'

urlpatterns = patterns('',
    # group subapp
    url(r'^group/$', views.group_info, name=search_group_prefix + 'info'),
    url(r'^group/create/$', views.create_group, name=search_group_prefix + 'create'),
    url(r'^group/manage/$', views.manage_group, name=search_group_prefix + 'manage'),
    url(r'^group/view/(?P<pk>\d+)/$', views.view_group,
        name=search_group_prefix + 'view'),
    url(r'^group/property/$', views.manage_property,
        name=search_group_prefix + 'manage-property'),
    # TODO: have the basic search page just be the search box instead of modal popup
    # needs to be on bottom
    url(r'^$', views.search, name='search'),
    url(r'^(?P<slug>\S+)/$', views.search, name='search')
)