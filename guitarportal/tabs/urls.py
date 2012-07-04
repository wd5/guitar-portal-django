# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail
from tabs.models import Artist
from tabs.views import artist_detail

artist_list = {
    'queryset': Artist.objects.order_by('name'),
    'template_name': 'artist_list.html',
    'template_object_name': 'artist',
    #'paginate_by': 100,
}

urlpatterns = patterns('',

    ('^$', list_detail.object_list, artist_list),
    ('^(?P<artist_name>.*)/$', artist_detail)
)
