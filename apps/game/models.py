# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models


# Create your models here.

# Game Table
class Game(models.Model):
    teamname1 = models.CharField(max_length=20, verbose_name=u'TeamName1', default=u'')
    teamname2 = models.CharField(max_length=20, verbose_name=u'TeamName2', default=u'')
    date = models.CharField(max_length=20, verbose_name=u'Date', default=datetime.now().strftime('%Y-%m-%d'))
    hour = models.CharField(max_length=20, verbose_name=u'Hour', default=datetime.now().strftime('%H:%M'))

    class Meta:
        verbose_name = u'Game'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'Game' + str(self.id)


# Player Table
class Player(models.Model):
    playerid = models.CharField(max_length=10, verbose_name=u'PlayerID', primary_key=True)
    name = models.CharField(max_length=30, verbose_name=u'Name', default=u'')
    position = models.CharField(max_length=20, verbose_name=u'Position', default=u'')
    teamname = models.CharField(max_length=20, verbose_name=u'TeamName', default=u'')
    value = models.IntegerField(verbose_name=u'Value', default=0)

    class Meta:
        verbose_name = u'Player'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# Point Table
class Point(models.Model):
    playerid = models.CharField(max_length=10, verbose_name=u'PlayerID', default=u'00000000')
    point = models.FloatField(verbose_name=u'Point', default=0)

    class Meta:
        verbose_name = u'Point'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'Player(' + self.playerid + u')'

