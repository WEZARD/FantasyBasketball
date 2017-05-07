# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render

from .models import UserMessage


# Create your views here.


def getform(request):
    if request.method == 'POST':
        zhongfeng = request.POST.get('zhongfeng_data')
        daqian = request.POST.get('daqian_data')
        xiaoqian = request.POST.get('xiaoqian_data')
        kongqiu = request.POST.get('kongqiu_data')
        defen = request.POST.get('defen_data')
        print zhongfeng
        print daqian
        print xiaoqian
        print kongqiu
        print defen
        user_message = UserMessage()
        user_message.name = zhongfeng
        user_message.message = daqian
        user_message.address = xiaoqian
        user_message.email = kongqiu
        user_message.save()

    # all_messages = UserMessage.objects.all()
    # message = None
    # all_messages = UserMessage.objects.filter(name='name2')
    # if all_messages:
    #     message = all_messages[0]
    #
    # data = {'send_message': message}
    # all_messages.delete()
    # for message in all_messages:
    #     print message.name


    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #
    #     user_message.save()

    # return render(request, 'message_form.html', data)
    return render(request, 'log_in.html')


def log_in(request):
    return render(request, 'log_in.html')


def register(request):
    return render(request, 'register.html')


def index(request):
    data = getData()
    return render(request, 'index.html', {'data': data})


def select_team(request):
    data = getData()
    return render(request, 'select_team.html', {'data': data})


def usercenter_info(request):
    data = getData()
    return render(request, 'usercenter-info.html', {'data': data})


def usercenter_history(request):
    data = getData()
    return render(request, 'usercenter-history.html', {'data': data})


def usercenter_rules(request):
    data = getData()
    return render(request, 'usercenter-rules.html', {'data': data})


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
