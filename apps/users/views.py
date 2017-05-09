# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend

from .models import UserProfile
from .forms import LoginForm
from .models import History, UserProfile

# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserProfile.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None


# Create your views here.
currentUser = None


# 用户登录页面
class LoginView(View):
    global currentUser

    def get(self, request):
        return render(request, 'log_in.html', {'msg': None})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            currentUser = authenticate(username=username, password=password)  # 返回成功为对象，失败为空
            if currentUser is not None:
                login(request, currentUser)
                data = {'userData': currentUser}
                return render(request, 'index.html', {'data': data})
        else:
            return render(request, 'log_in.html', {'msg': 'Invalid username or password!'})


# 用户注册页面
def register(request):
    return render(request, 'register.html')


# 用户中心信息页面
def usercenter_info(request):
    data = getData()
    return render(request, 'usercenter-info.html', {'data': data})


# 用户中心游戏历史页面
def usercenter_history(request):
    user = UserProfile.objects.get(username='admin')
    historyData = getHistory(user)
    userData = getUserData()
    data = {'userData': userData, 'historyData': historyData}

    if request.method == 'POST':
        c = request.POST.get('c_data')
        pf = request.POST.get('pf_data')
        sf = request.POST.get('sf_data')
        sg = request.POST.get('sg_data')
        pg = request.POST.get('pg_data')

        if (c is None or c == '') or (pf is None or pf == '') or (sf is None or sf == '') or (
                        sg is None or sg == '') or (pg is None or pg == ''):
            return render(request, 'usercenter-history.html', {'data': data})

        add_time = datetime.now().strftime('%Y-%m-%d')
        user = UserProfile.objects.get(username='admin')

        record = History()
        record.add_time = add_time
        record.c_name = c
        record.pf_name = pf
        record.sf_name = sf
        record.sg_name = sg
        record.pg_name = pg
        record.user = user
        record.save()

    return render(request, 'usercenter-history.html', {'data': data})


# 用户中心游戏规则页面
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


# 获取历史记录数据
def getHistory(user):
    all_records = History.objects.filter(user=user)

    return all_records
