# -*- coding: utf-8 -*-

from django.contrib import admin
from tabs.models import Album, Artist, Chord, GuitarPro, Song, Tab

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Chord)
admin.site.register(GuitarPro)
admin.site.register(Song)
admin.site.register(Tab)