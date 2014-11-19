from django.conf.urls import patterns, url

from foodbank import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)