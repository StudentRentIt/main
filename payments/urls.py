from django.conf.urls import patterns, url

from payments import views

urlpatterns = patterns('',
    # General Views
    url(r'^$', views.payment, name='payment'),
)