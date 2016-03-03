from django.conf.urls import url
from django.contrib import admin

from .views import (
	dash_list,
	dash_create,
	# dash_detail,
	dash_chart,
	# post_update,
	# post_delete,
	)

urlpatterns = [
	url(r'^$', dash_list, name='list'),
    url(r'^create/$', dash_create),
    url(r'^chart/$', dash_chart),
    # url(r'^(?P<id>\d+)$', dash_detail, name='detail'),
    # url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    # url(r'^(?P<id>\d+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
