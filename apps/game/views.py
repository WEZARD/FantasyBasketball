# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render


# Create your views here.


# 大厅页面
def index(request):
    data = getData()
    return render(request, 'index.html', {'data': data})


# 选择球队页面
def select_team(request):
    data = getData()
    return render(request, 'select_team.html', {'data': data})


# 从数据库获取数据，处理后返回给前台显示
def getData():
    # 用户数据，用于显示于右上角的框框
    userName = 'userName1'
    userPassword = 'password1'
    userSex = 0
    userAddress = 'User1 Address'
    userEmail = 'user1@user1.com'
    userMoney = 'userMoney1'
    userPicture = 'userhead.JPG'
    userData = {'userName': userName, 'userPassword': userPassword, 'userSex': userSex, 'userAddress': userAddress,
                'userEmail': userEmail, 'userMoney': userMoney, 'userPicture': userPicture}

    # 比赛数据，用于显示在主页的列表中
    deadline = random.randint(0, 24)
    gamePic = random.randint(0, 1)
    gameAward = random.randint(50, 70)
    gameRequired = random.randint(20, 30)
    gameProb = random.randint(10, 90)
    totalPeople = random.randint(1000, 3000)
    gameData = {'deadline': deadline, 'gamePic': gamePic, 'gameAward': gameAward,
                'gameRequired': gameRequired, 'gameProb': gameProb, 'totalPeople': totalPeople}

    # 球员数据

    data = {'userData': userData, 'gameData': gameData}
    return data