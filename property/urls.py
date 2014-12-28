from django.conf.urls import patterns, url

from property import views


urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/(?P<slug>\S+)/community/$', views.community,
        name="property-community"),
    url(r'^manage/$', views.ManagePropertyTemplateView.as_view(), 
        name="manage-property"),
    url(r'^add/$', views.PropertyCreateView.as_view(), #views.addproperty,
        name="add-property"),
    (r'^update/$', views.updateproperty),
    url(r'^update/(?P<pk>\d+)/$', views.updateproperty,
        name="update-property"),
    url(r'^update/(\d+)/(\S+)/(\d+)/$', views.updateproperty,
        name="property-type"),
    url(r'^update/(\d+)/(\S+)/(\d+)/(\S+)/$', views.updateproperty,
        name="property-type-delete"),
    (r'^update/(\d+)/(\S+)/$', views.updateproperty),
    url(r'^(?P<pk>\d+)/(?P<slug>[a-zA-Z0-9][ A-Za-z0-9_-]+)/(?P<action>\S+)/$', views.property,
        name="property-action"),
    url(r'^(?P<pk>\d+)/(?P<slug>\S+)/$', views.property,
        name="property"),
    url(r'^business/(?P<pk>\d+)/(?P<slug>\S+)/$', views.BusinessDetailView.as_view(),
        name="business"),
    url(r'^favorites/$', views.favorites, name="favorites"),
    (r'^favorites/(\d+)/$', views.favorites),
    url(r'^favorites/(\S+)/$', views.favorite, name="favorite-action"),
)