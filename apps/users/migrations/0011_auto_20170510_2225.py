# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170510_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.CharField(default='static/images/default_user.png', max_length=150, verbose_name='image'),
        ),
    ]
