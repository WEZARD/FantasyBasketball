# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import UserMessage

# Create your views here.


def getform(request):
    if request.method == 'POST':
        zhongfeng = request.POST.get('zhongfeng_data');
        daqian = request.POST.get('daqian_data');
        xiaoqian = request.POST.get('xiaoqian_data');
        kongqiu = request.POST.get('kongqiu_data');
        defen = request.POST.get('defen_data');
        print zhongfeng
        print daqian
        print xiaoqian
        print kongqiu
        print defen

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


def index(request):
    test = [1, 2, 3]
    return render(request, 'index.html', {'test': test})


def select_team(request):
    return render(request, 'select_team.html')


def usercenter_info(request):
    return render(request, 'usercenter-info.html')


def usercenter_history(request):
    return render(request, 'usercenter-history.html')


def usercenter_rules(request):
    return render(request, 'usercenter-rules.html')