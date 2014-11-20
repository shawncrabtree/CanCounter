from django.conf.urls import patterns, url

from foodbank import views
from foodbank.views import Inventory

urlpatterns = patterns('',
    url(r'^login/', views.login, name='login'),
    url(r'^inventory/', Inventory.as_view(), name='item_list'),
    url(r'^hello/', views.hello, name='hello'),
)