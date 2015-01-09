from django.conf.urls import patterns, url

from . import views


prefix = "re-"

urlpatterns = patterns('',
    url(r'^(?P<slug>\S+)/properties/$', views.CompanyPropertiesListView.as_view(), 
        name=prefix + "company-properties"),
    url(r'^(?P<slug>\S+)/members/$', views.company_members, 
        name=prefix + "company-members"),
    url(r'^(?P<slug>\S+)/support/$', views.CompanySupportTemplateView.as_view(), 
        name=prefix + "company-support"),
    url(r'^(?P<slug>\S+)/$', views.CompanyHomeFormView.as_view(), 
        name=prefix + "company-home"),

    url(r'^$', views.HomeTemplateView.as_view(), name=prefix + "home"),
)