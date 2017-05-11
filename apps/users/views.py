# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend

from .models import UserProfile
from .forms import LoginForm, RegisterForm
from .models import History, UserProfile
from game.models import Player
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

                # session for saving data
                setSession(request, currentUser)

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
            # session for saving data
            setSession(request, new_user)

            login_code = 0
            gameData = getGameData()
            data = {'userData': new_user, 'gameData': gameData, 'code': login_code}
            return render(request, 'index.html', {'data': data})
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
    return render(request, 'register.html', {'data': data})


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

        c_score = Player.objects.get(name=c).fantasy_score
        pf_score = Player.objects.get(name=pf).fantasy_score
        sf_score = Player.objects.get(name=sf).fantasy_score
        sg_score = Player.objects.get(name=sg).fantasy_score
        pg_score = Player.objects.get(name=pg).fantasy_score

        record = History(add_time=add_time, c_name=c, pf_name=pf, sf_name=sf, sg_name=sg, pg_name=pg, user=user,
                         c_score=c_score, pf_score=pf_score, sf_score=sf_score, sg_score=sg_score, pg_score=pg_score)
        record.save()

        historyData = getHistory(user)
        data = {'userData': userData, 'historyData': historyData}
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


# 获取历史记录数据
def getHistory(user):
    all_records = History.objects.filter(user=user)

    return all_records


# 设置用户session
def setSession(request, user):
    request.session['username'] = user.username
    request.session['money'] = user.money
    request.session['email'] = user.email
    request.session['gender'] = user.gender
    request.session['image'] = user.image
    request.session['address'] = user.address


# 更新数据
def updateScore(request):
    recordID = request.GET.get('recordID', None)
    if recordID is not None:
        record = History.objects.get(id=recordID)
        c_score = record.c_score
        pf_score = record.pf_score
        sf_score = record.sf_score
        sg_score = record.sg_score
        pg_score = record.pg_score
        data = {'c_score': c_score, 'pf_score': pf_score, 'sf_score': sf_score, 'sg_score': sg_score,
                'pg_score': pg_score}
        return JsonResponse(data)
