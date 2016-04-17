# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 01:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wangblog', '0004_auto_20160416_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 1, 52, 6, 276869), verbose_name='date joined'),
        ),
    ]
