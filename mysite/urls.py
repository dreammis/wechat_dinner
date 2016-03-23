from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wechat/', include('wechat.urls', namespace='wechat')),
    url(r'^res/', include('res.urls', namespace='res')),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT + "/css/"}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT + "/js/"}),
    url(r'^image/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT + "/image/"}),
)
