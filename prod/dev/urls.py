from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView
from main import urls as mainurls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    url(r'^', include(mainurls)),

    #internal apps
    (r'^internal/tasks/', include('flowtask.urls')),
    (r'^internal/reports/', include('flowreport.urls')),
)
