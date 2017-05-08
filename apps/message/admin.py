# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserMessage

# Register your models here.


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'message']
    search_fields = ['name', 'email', 'address', 'message']


admin.site.register(UserMessage, UserMessageAdmin)