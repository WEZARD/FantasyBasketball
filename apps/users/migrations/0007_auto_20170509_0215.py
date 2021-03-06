# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170509_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='c_id',
        ),
        migrations.RemoveField(
            model_name='history',
            name='pf_id',
        ),
        migrations.RemoveField(
            model_name='history',
            name='pg_id',
        ),
        migrations.RemoveField(
            model_name='history',
            name='sf_id',
        ),
        migrations.RemoveField(
            model_name='history',
            name='sg_id',
        ),
        migrations.AddField(
            model_name='history',
            name='c_name',
            field=models.CharField(default='', max_length=10, verbose_name='Center_Name'),
        ),
        migrations.AddField(
            model_name='history',
            name='pf_name',
            field=models.CharField(default='', max_length=10, verbose_name='PF_Name'),
        ),
        migrations.AddField(
            model_name='history',
            name='pg_name',
            field=models.CharField(default='', max_length=10, verbose_name='PG_Name'),
        ),
        migrations.AddField(
            model_name='history',
            name='sf_name',
            field=models.CharField(default='', max_length=10, verbose_name='SF_Name'),
        ),
        migrations.AddField(
            model_name='history',
            name='sg_name',
            field=models.CharField(default='', max_length=10, verbose_name='SG_Name'),
        ),
    ]
