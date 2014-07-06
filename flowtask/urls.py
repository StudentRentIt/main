from django.conf.urls import patterns, url

from flowtask.views import TaskListView, TaskUpdateView, TaskActionListView, \
    TaskCreateView

urlpatterns = patterns('',
    ##### Task Views #####
    url(r'^$',  TaskListView.as_view(), name='task-list'),
    url(r'create/$',  TaskCreateView.as_view(), name='task-create'),
    url(r'update/(?P<pk>\d+)/$', TaskUpdateView.as_view(), name='task-update'),
    url(r'(?P<action>\D+)/(?P<pk>\d+)/$', TaskActionListView.as_view(), name='task-action'),

    ##### Project Views #####
)