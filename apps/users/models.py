# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    gender = models.IntegerField(choices=((0, 'male'), (1, 'female')), default=0)
    address = models.CharField(max_length=100, default=u'')
    image = models.ImageField(upload_to='image/%Y/%m', default=u'/static/images/userhead.JPG')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# 生成的每条记录，用来显示用户游戏历史
class History(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'user')  # 生成记录对应的用户
    add_time = models.DateTimeField(verbose_name='add_time', default=datetime.now)
    is_win = models.CharField(max_length=5, choices=(('win', 'win'), ('lose', 'lose')), default=-1)
    award = models.IntegerField(verbose_name='award', default=0)
    center = models.CharField(max_length=30, verbose_name='center')
    p_forward = models.CharField(max_length=30, verbose_name='p_forward')
    s_forward = models.CharField(max_length=30, verbose_name='s_forward')
    s_guard = models.CharField(max_length=30, verbose_name='s_guard')
    p_guard = models.CharField(max_length=30, verbose_name='p_guard')

    class Meta:
        verbose_name = 'History Record'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.user, self.is_win)

