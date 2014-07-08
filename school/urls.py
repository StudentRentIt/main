from django.conf.urls import patterns, url

from school import views


urlpatterns = patterns('',
    #School Info - urls to show the base of school info
    url(r'^(?P<pk>\d+)/(?P<slug>[a-zA-Z0-9\-]+)/(?P<type>articles)/$',
        views.SchoolArticleCreateView.as_view(), name="school-articles"),
    url(r'^(?P<pk>\d+)/(?P<slug>[a-zA-Z0-9\-]+)/(?P<type>events)/$',
        views.SchoolEventCreateView.as_view(), name="school-events"),
    url(r'^(?P<pk>\d+)/(?P<slug>[a-zA-Z0-9\-]+)/(?P<type>deals)/$',
        views.SchoolDealCreateView.as_view(), name="school-deals"),
    url(r'^(?P<pk>\d+)/(?P<slug>[a-zA-Z0-9\-]+)/(?P<type>roommates)/$',
        views.SchoolRoommateCreateView.as_view(), name="school-roommates"),

    #school update views - allows updating of articles
    url(r'^update/articles/(?P<pk>\d+)/$', views.ArticleUpdateView.as_view(),
        name="update-article"),
    url(r'^update/events/(?P<pk>\d+)/$', views.EventUpdateView.as_view(),
        name="update-event"),
    url(r'^update/deals/(?P<pk>\d+)/$', views.DealUpdateView.as_view(),
        name="update-deal"),
    url(r'^update/roommates/(?P<pk>\d+)/$', views.RoommateUpdateView.as_view(),
        name="update-roommate"),

    #school update list views - shows what is possible to update
    url(r'^update/articles/$', views.ArticleUpdateListView.as_view(),
        name="update-articles"),
    url(r'^update/events/$', views.EventUpdateListView.as_view(),
        name="update-events"),
    url(r'^update/deals/$', views.DealUpdateListView.as_view(),
        name="update-deals"),
    url(r'^update/roommates/$', views.RoommateUpdateListView.as_view(),
        name="update-roommates"),

    #this URL needs to stay at the bottom of the url list
    url(r'^(?P<pk>\d+)/(?P<slug>[a-zA-Z0-9\-]+)/',
        views.SchoolRedirectView.as_view()),
)