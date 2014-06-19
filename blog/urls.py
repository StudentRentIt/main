from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='blog-home'),
    url(r'article/(?P<pk>\d+)/(?P<slug>\S+)/$', views.article, name='blog-article'),
    url(r'(?P<type>[a-zA-Z0-9][ A-Za-z0-9_-]+)/(?P<pk>\d+)/(?P<slug>\S+)/$',
        views.type, name='blog-type'),
)