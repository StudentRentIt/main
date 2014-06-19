from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from main import views


urlpatterns = patterns('',
    url(r'^$', views.HomeListView.as_view(), name='home-list'),
    url(r'^search/$', views.search, name="search"),
    url(r'^search/(?P<pk>\d+)/(?P<slug>\D+)/$', views.search, name="search"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact-view"),
    url(r'^schools/$', TemplateView.as_view(
        template_name="maincontent/school_list.html"), name="school-list"),
    url(r'^schools/(?P<pk>\d+)/$', views.property_list, name="property-list"),
    url(r'^accounts/profile/$', views.ProfileUpdateView.as_view(), name="user_profile"),
    url(r'^mongoose/$', TemplateView.as_view(
        template_name='maincontent/mongoose_analytics.html'), name='mongoose-analytics'),
    url(r'^howitworks/$', TemplateView.as_view(
        template_name="maincontent/howitworks.html"), name="how-it-works"),
    (r'^about/$', views.ContactView.as_view(template_name="maincontent/about.html")),
    (r'^privacy/$', TemplateView.as_view(template_name="maincontent/privacy.html")),
    (r'^terms/$', TemplateView.as_view(template_name="maincontent/terms.html")),

    #payments
    url(r'^payment/$', views.onetime_payment, name='payment'),
)