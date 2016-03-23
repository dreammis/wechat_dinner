# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('res.views',
    url(r'^$', 'index'),
    url(r'^jsonp$', 'food_list'),
    url(r'^buy', 'buy'),
)