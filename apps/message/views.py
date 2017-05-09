# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

    # return render(request, 'message_form.html', data)
    return render(request, 'message_form.html')

