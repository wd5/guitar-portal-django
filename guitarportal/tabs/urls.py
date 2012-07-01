# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

from tabs.views import artist_list 

urlpatterns = patterns('',

    url(r'^$', ),
    url(r'^tabs/', include('guitarportal.foo.urls')),

)
