# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20170508_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.CharField(default=b'2017-05-09', max_length=20, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='game',
            name='hour',
            field=models.CharField(default=b'02:01', max_length=20, verbose_name='Hour'),
        ),
    ]
