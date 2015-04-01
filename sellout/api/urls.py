from django.conf.urls import patterns

from sellout.api import all_endpoints


endpoints = list(all_endpoints())
urlpatterns = patterns('', *endpoints)

