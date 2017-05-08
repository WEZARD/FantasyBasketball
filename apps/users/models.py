# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# User Table
class UserProfile(AbstractUser):
    upload_dir = 'static/img/upload'
    default_pic = 'static/images/default_user.png'

    gender = models.IntegerField(choices=((0, u'male'), (1, u'female')), default=0)
    address = models.CharField(max_length=100, default=u'')
    image = models.ImageField(upload_to=upload_dir, default=default_pic)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# History Table
class History(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'user')
    add_time = models.CharField(max_length=20, verbose_name=u'add_time', default=datetime.now().strftime('%Y-%m-%d'))
    is_win = models.CharField(max_length=5, choices=((u'win', u'win'), (u'lose', u'lose')), default=u'win')
    award = models.IntegerField(verbose_name='award', default=0)

    center_id = models.CharField(max_length=10, verbose_name=u'CenterID', default=u'00000000')
    p_forward_id = models.CharField(max_length=10, verbose_name=u'P_ForwardID', default=u'00000000')
    s_forward_id = models.CharField(max_length=10, verbose_name=u'S_ForwardID', default=u'00000000')
    s_guard_id = models.CharField(max_length=10, verbose_name=u'S_GuardID', default=u'00000000')
    p_guard_id = models.CharField(max_length=10, verbose_name=u'P_GuardID', default=u'00000000')
    total_point = models.FloatField(verbose_name=u'Sum', default=0)

    class Meta:
        verbose_name = 'History Record'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.user, self.is_win)

