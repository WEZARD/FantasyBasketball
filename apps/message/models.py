# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"username")
    email = models.EmailField(verbose_name=u"email")
    address = models.CharField(max_length=100, verbose_name=u"address")
    message = models.CharField(max_length=500, verbose_name=u"message")

    class Meta:
        verbose_name = u"message"
