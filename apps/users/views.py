# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend

from .models import UserProfile
from .forms import LoginForm


# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserProfile.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None


# Create your views here.


# 用户登录页面
class LoginView(View):
    def get(self, request):
        return render(request, 'log_in.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)  # 返回成功为对象，失败为空
            if user is not None:
                login(request, user)
                data = getData()
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
    data = getData()
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