# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserProfile, History


# Register your models here.


# Register UserProfile Table
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender', 'email', 'address', 'image']
    search_fields = ['username', 'gender', 'email', 'address', 'image']
    list_filter = ['username', 'gender', 'email', 'address', 'image']


# Register History Table
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'add_time', 'is_win', 'award', 'center_id', 'p_forward_id', 's_forward_id', 's_guard_id',
                    'p_guard_id', 'total_point']
    search_fields = ['user', 'add_time', 'is_win', 'award', 'center_id', 'p_forward_id', 's_forward_id', 's_guard_id',
                    'p_guard_id', 'total_point']
    list_filter = ['user', 'add_time', 'is_win', 'award', 'center_id', 'p_forward_id', 's_forward_id', 's_guard_id',
                    'p_guard_id', 'total_point']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(History, HistoryAdmin)
