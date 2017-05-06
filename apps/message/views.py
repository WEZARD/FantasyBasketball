# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import UserMessage

# Create your views here.


def getform(request):
    # all_messages = UserMessage.objects.all()
    message = None
    all_messages = UserMessage.objects.filter(name='name2')
    if all_messages:
        message = all_messages[0]

    data = {'send_message': message}
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

    return render(request, 'message_form.html', data)


def index(request):
    return render(request, 'index.html')
