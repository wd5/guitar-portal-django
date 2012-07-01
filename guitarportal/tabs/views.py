# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from urllib import unquote

from tabs.models import Artist
from externals.formview import formview



@formview
def artist_list(request):
    #form = EditForm(id, request.POST or None)

    def get():
        artists = Artist.objects.order_by("name")
        return render_to_response(
                request,
                template = "tabs/templates/artist_list.html",
                context = {
                    "artist_list": artists,
                },
        )

    def post():
        pass
    
    return get, post

@formview
def artist_detail(request, name):
    artist = get_object_or_404(Artist, name=unquote(name))

    def get():
        return render_to_response(
            template = "tabs/templates/artist_detail.html",
            context = {
                "artist": artist,
            },
        )

    def post():
        pass

    return get, post
