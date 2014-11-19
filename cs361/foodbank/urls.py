from django.conf.urls import patterns, url

from foodbank import views
from foodbank.views import Inventory

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^inventory/', Inventory.as_view(), name='item_list'),
)