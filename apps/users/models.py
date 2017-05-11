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
    money = models.IntegerField(verbose_name=u'UserMoney', default=200)
    # image = models.ImageField(upload_to=upload_dir, default=default_pic)
    image = models.CharField(max_length=150, verbose_name=u'image', default=default_pic)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# History Table
class History(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'user')
    add_time = models.CharField(max_length=20, verbose_name=u'add_time', default=datetime.now().strftime('%Y-%m-%d'))
    is_win = models.CharField(max_length=10, verbose_name=u'result', default=u'pending')
    award = models.IntegerField(verbose_name='award', default=0)
    picture = models.IntegerField(verbose_name=u'GamePicture', default=1)

    c_name = models.CharField(max_length=10, verbose_name=u'Center_Name', default=u'')
    pf_name = models.CharField(max_length=10, verbose_name=u'PF_Name', default=u'')
    sf_name = models.CharField(max_length=10, verbose_name=u'SF_Name', default=u'')
    sg_name = models.CharField(max_length=10, verbose_name=u'SG_Name', default=u'')
    pg_name = models.CharField(max_length=10, verbose_name=u'PG_Name', default=u'')
    total_point = models.FloatField(verbose_name=u'Sum', default=0)

    class Meta:
        verbose_name = 'History Record'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.user, self.is_win)

