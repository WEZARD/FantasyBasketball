# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20170511_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='IsGameOver',
            field=models.CharField(default='false', max_length=10, verbose_name='IsGameOver'),
        ),
    ]