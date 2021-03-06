# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170508_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'History Record', 'verbose_name_plural': 'History Record'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profile'},
        ),
        migrations.RemoveField(
            model_name='history',
            name='center',
        ),
        migrations.RemoveField(
            model_name='history',
            name='p_forward',
        ),
        migrations.RemoveField(
            model_name='history',
            name='p_guard',
        ),
        migrations.RemoveField(
            model_name='history',
            name='s_forward',
        ),
        migrations.RemoveField(
            model_name='history',
            name='s_guard',
        ),
        migrations.AddField(
            model_name='history',
            name='center_id',
            field=models.CharField(default='00000000', max_length=10, verbose_name='CenterID'),
        ),
        migrations.AddField(
            model_name='history',
            name='p_forward_id',
            field=models.CharField(default='00000000', max_length=10, verbose_name='P_ForwardID'),
        ),
        migrations.AddField(
            model_name='history',
            name='p_guard_id',
            field=models.CharField(default='00000000', max_length=10, verbose_name='P_GuardID'),
        ),
        migrations.AddField(
            model_name='history',
            name='s_forward_id',
            field=models.CharField(default='00000000', max_length=10, verbose_name='S_ForwardID'),
        ),
        migrations.AddField(
            model_name='history',
            name='s_guard_id',
            field=models.CharField(default='00000000', max_length=10, verbose_name='S_GuardID'),
        ),
        migrations.AddField(
            model_name='history',
            name='total_point',
            field=models.FloatField(default=0, verbose_name='Sum'),
        ),
        migrations.AlterField(
            model_name='history',
            name='add_time',
            field=models.CharField(default=b'2017-05-08', max_length=20, verbose_name='add_time'),
        ),
        migrations.AlterField(
            model_name='history',
            name='is_win',
            field=models.CharField(choices=[('win', 'win'), ('lose', 'lose')], default='win', max_length=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='../../static/images/default_user.png', upload_to='../../static/img/upload'),
        ),
    ]
