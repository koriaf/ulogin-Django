# -*- coding: utf-8 -*-

try:
    from django.conf.urls.defaults import url, patterns
except ImportError:
    from django.conf.urls import patterns, url


urlpatterns = patterns('django_ulogin.views',
    url('^postback/$', 'postback', name='ulogin_postback'),
    url('^ulogin_xd.html$', 'ulogin_xd', name='ulogin_xd'),
)