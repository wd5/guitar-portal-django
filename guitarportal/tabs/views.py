# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from urllib import unquote

from tabs.models import Artist
from externals.formview import formview

def something_list(request, queryset, template):
    things = list(queryset)
    return render_to_response(template, {
            "thing_list": things
    })

@formview
def artist_list(request):
    #form = EditForm(id, request.POST or None)

    def get():
        return something_list(request,
                              Artist.objects.order_by("name"),
                              "tabs/templates/artist_list.html"
        )

    def post():
        pass
    
    return get, post

@formview
def artist_detail(request, artist_name):
    artist = get_object_or_404(Artist, name=unquote(artist_name))
    def get():
        return render_to_response(
            "artist_detail.html",
            {
                "artist": artist,
            }
        )

    def post():
        pass

    return get, post
