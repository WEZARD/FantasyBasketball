# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserProfile, History

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender', 'email', 'address', 'image']
    search_fields = ['username', 'gender', 'email', 'address', 'image']
    list_filter = ['username', 'gender', 'email', 'address', 'image']


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'add_time', 'is_win', 'award', 'center', 'p_forward', 's_forward', 's_guard', 'p_guard']
    search_fields = ['user', 'is_win', 'award', 'center', 'p_forward', 's_forward', 's_guard', 'p_guard']
    list_filter = ['user', 'add_time', 'is_win', 'award', 'center', 'p_forward', 's_forward', 's_guard', 'p_guard']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(History, HistoryAdmin)