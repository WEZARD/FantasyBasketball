# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170510_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='picture',
            field=models.IntegerField(default=1, verbose_name='GamePicture'),
        ),
    ]
