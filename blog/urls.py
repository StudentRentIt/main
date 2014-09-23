from django.conf.urls import patterns, url

from blog import views

app_prefix = 'blog-'

urlpatterns = patterns('',
    url(r'^$', views.home, name=app_prefix + 'home'),
    url(r'article/(?P<pk>\d+)/(?P<slug>\S+)/$', views.article, name=app_prefix + 'article'),
    url(r'(?P<type>[ A-Za-z0-9_-]+)/(?P<pk>\d+)/(?P<slug>\S+)/$',
        views.type, name=app_prefix + 'type'),
)