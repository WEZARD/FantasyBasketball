# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_userprofile_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='add_time',
            field=models.CharField(default=b'2017-05-12', max_length=20, verbose_name='add_time'),
        ),
    ]
