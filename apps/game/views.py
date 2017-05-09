# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime
from .models import Game, Player, Point

from django.shortcuts import render
from django.db.models import Q


# Create your views here.


# 大厅页面
def index(request):
    userData = getUserData()
    gameData = getGameData()

    data = {'userData': userData, 'gameData': gameData}

    return render(request, 'index.html', {'data': data})


# 选择球队页面
def select_team(request):
    if request.method == 'POST':
        team1 = request.POST.get('team1')
        team2 = request.POST.get('team2')
        playerData = getPlayerData(team1, team2)
        userData = getUserData()

    data = {'userData': userData, 'playerData': playerData}
    return render(request, 'select_team.html', {'data': data})


# 获取用户数据
def getUserData():
    userName = 'userName1'
    userPassword = 'password1'
    userSex = 0
    userAddress = 'User1 Address'
    userEmail = 'user1@user1.com'
    userMoney = 'userMoney1'
    userPicture = 'userhead.JPG'
    userData = {'userName': userName, 'userPassword': userPassword, 'userSex': userSex, 'userAddress': userAddress,
                'userEmail': userEmail, 'userMoney': userMoney, 'userPicture': userPicture}

    return userData


# 获取比赛数据
def getGameData():
    gameData = None
    present_date = datetime.now().strftime('%Y-%m-%d')
    present_hour = datetime.now().strftime('%H:%M')
    # all_games = Game.objects.filter(date=present_date)
    all_games = Game.objects.all()
    if all_games:
        # for game in all_games:
        #     if present_hour > game.hour:
        #         all_games.delete()
        gameData = all_games

    return gameData


# 获取球员数据
def getPlayerData(team1, team2):
    all_players = Player.objects.filter(Q(teamname=team1) | Q(teamname=team2))
    c_players = all_players.filter(position='c')
    pf_players = all_players.filter(position='pf')
    sf_players = all_players.filter(position='sf')
    pg_players = all_players.filter(position='pg')
    sg_players = all_players.filter(position='sg')
    playerData = {'c_players': c_players, 'pf_players': pf_players, 'sf_players': sf_players, 'pg_players': pg_players,
                  'sg_players': sg_players}

    return playerData
