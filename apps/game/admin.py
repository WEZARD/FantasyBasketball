# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Game, Player, Point

# Register your models here.


# Register Game Table
class GameAdmin(admin.ModelAdmin):
    list_display = ['teamname1', 'teamname2', 'date', 'hour']
    search_fields = ['teamname1', 'teamname2', 'date', 'hour']
    list_filter = ['teamname1', 'teamname2', 'date', 'hour']


# Register Player Table
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['playerid', 'name', 'position', 'teamname', 'value']
    search_fields = ['playerid', 'name', 'position', 'teamname', 'value']
    list_filter = ['playerid', 'name', 'position', 'teamname', 'value']


# Register Point Table
class PointAdmin(admin.ModelAdmin):
    list_display = ['playerid', 'point']
    search_fields = ['playerid', 'point']
    list_filter = ['playerid', 'point']


admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Point, PointAdmin)
