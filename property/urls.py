from django.conf.urls import patterns, url

from property import views

from flowreport.views import PropertySummaryListView


urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/(?P<slug>\S+)/community/$', views.community,
        name="property-community"),
    (r'^manage/$', views.ManagePropertyTemplateView.as_view()),
    url(r'^add/$', views.PropertyCreateView.as_view(), #views.addproperty,
        name="add-property"),

    # urls used to update property information
    (r'^update/$', views.updateproperty),
    url(r'^update/(?P<pk>\d+)/$', views.updateproperty,
        name="update-property"),
    url(r'^update/(\d+)/(\S+)/(\d+)/$', views.updateproperty,
        name="property-type"),
    url(r'^update/(\d+)/(\S+)/(\d+)/(\S+)/$', views.updateproperty,
        name="property-type-delete"),
    (r'^update/(\d+)/(\S+)/$', views.updateproperty),
    url(r'^(?P<pk>\d+)/(?P<slug>\S+)/summary/$', PropertySummaryListView.as_view(),
        name="property-summary"),

    url(r'^(?P<pk>\d+)/(?P<slug>[a-zA-Z0-9][ A-Za-z0-9_-]+)/(?P<action>\S+)/$', views.property,
        name="property-action"),
    url(r'^(?P<pk>\d+)/(?P<slug>\S+)/$', views.property,
        name="property"),
    url(r'^business/(?P<pk>\d+)/(?P<slug>\S+)/summary/$', PropertySummaryListView.as_view(),
        name="business-summary"),
    url(r'^business/(?P<pk>\d+)/(?P<slug>\S+)/$', views.BusinessDetailView.as_view(),
        name="business"),

    # urls used to keep user preferences, favorites and hidden
    url(r'^favorites/$', views.favorites, name="favorites"),
    (r'^favorites/(\d+)/$', views.favorites),
    url(r'^favorites/(\S+)/$', views.favorite, name="favorite-action"),
    url(r'^toggle/(?P<pk>\d+)/$', views.toggle_property, name="toggle-property"),
    url(r'^hidden/$', views.hidden_properties, name="hidden-properties"),

    # urls used for payment functionality. Not currently used and might be removed at some point.
    url(r'^update/(?P<pk>\d+)/services/recurring/$', views.recurring_services,
        name="update-property-recurring-services"),
    url(r'^update/(?P<pk>\d+)/services/onetime/$', views.onetime_services,
        name="update-property-onetime-services"),
)