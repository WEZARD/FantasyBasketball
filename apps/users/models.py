# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    gender = models.CharField(max_length=5, choices=((0, 'male'), (1, 'female')), default=0)
    # address = models.CharField(max_length=100, default=u'')
    # image = models.ImageField(upload_to='image/%Y/%m', default=u'/static/images/userhead.JPG')
    #
    # class Meta:
    #     verbose_name = 'user_profile'
    #     verbose_name_plural = verbose_name
    #
    # def __unicode__(self):
    #     return self.username


