# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend

from .models import UserProfile
from .forms import LoginForm, RegisterForm
from .models import History, UserProfile
from game.views import getGameData, getUserData

# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserProfile.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None


# Create your views here.

def test(request):
    return render(request, '123.html')


# 用户登录页面
class LoginView(View):

    def get(self, request):
        return render(request, 'log_in.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            currentUser = authenticate(username=username, password=password)  # 返回成功为对象，失败为空
            if currentUser is not None:
                login_code = 0
                login(request, currentUser)

                # session for save data
                request.session['username'] = currentUser.username
                request.session['money'] = currentUser.money
                request.session['email'] = currentUser.email
                request.session['gender'] = currentUser.gender
                request.session['image'] = currentUser.image
                request.session['address'] = currentUser.address

                gameData = getGameData()
                data = {'userData': currentUser, 'gameData': gameData, 'code': login_code}
                return render(request, 'index.html', {'data': data})

        login_code = 1  # 提示用户登录失败
        data = {'code': login_code}
        return render(request, 'log_in.html', {'data': data})


# 用户注册页面
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('email', '')
            password = request.POST.get('password', '')

            new_user = UserProfile()
            new_user.username = username
            new_user.email = username
            new_user.password = make_password(password)
            new_user.save()
            return render(request, 'register.html', {'register_form': register_form})
        else:
            register_code = -1
            data = {'code': register_code}
            return render(request, 'register.html', {'data': data})

        # return render(request, 'register.html', {'register_form': register_form})


# 用户注册页面
def register(request):
    if request.method == 'POST':
        register_name = request.POST.get('email')
        print register_name
        already_name = UserProfile.objects.filter(Q(username=register_name) | Q(email=register_name))
        print already_name
        if already_name is not None:  # 数据库已存在
            register_code = 1
            data = {'code': register_code}
            return render(request, 'register.html', {'data': data})
        else:
            password = request.POST.get('password')
            print register_name
            print password
            newUser = UserProfile()
            newUser.email = register_name
            newUser.password = password
            # newUser.save()
            currentUser = newUser

            gameData = getGameData()
            register_code = 0
            data = {'userData': currentUser, 'gameData': gameData, 'code': register_code}
            return render(request, 'index.html', {'data': data})

    register_code = 0
    data = {'code': register_code}
    return render(request, 'register.html', {'data':data})


# 用户中心信息页面
class UserInfoView(View):
    def get(self, request):
        # gameData = getGameData()
        userData = getUserData(request)
        data = {'userData': userData}

        return render(request, 'usercenter-info.html', {'data': data})


# 用户中心游戏历史页面
class UserHistoryView(View):
    def post(self, request):
        userData = getUserData(request)
        user = UserProfile.objects.get(username=userData['username'])
        historyData = getHistory(user)
        data = {'userData': userData, 'historyData': historyData}

        c = request.POST.get('c_data')
        pf = request.POST.get('pf_data')
        sf = request.POST.get('sf_data')
        sg = request.POST.get('sg_data')
        pg = request.POST.get('pg_data')

        if (c is None or c == '') or (pf is None or pf == '') or (sf is None or sf == '') or (
                        sg is None or sg == '') or (pg is None or pg == ''):
            return render(request, 'usercenter-history.html', {'data': data})

        add_time = datetime.now().strftime('%Y-%m-%d')
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

    def get(self, request):
        userData = getUserData(request)
        user = UserProfile.objects.get(username=userData['username'])
        historyData = getHistory(user)
        data = {'userData': userData, 'historyData': historyData}
        return render(request, 'usercenter-history.html', {'data': data})

# 用户中心游戏规则页面
class UserRulesView(View):
    def get(self, request):
        userData = getUserData(request)
        data = {'userData': userData}

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


# 获取历史记录数据
def getHistory(user):
    all_records = History.objects.filter(user=user)

    return all_records
