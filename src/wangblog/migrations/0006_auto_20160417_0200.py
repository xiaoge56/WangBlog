# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 02:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wangblog', '0005_auto_20160417_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 2, 0, 26, 210262), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=123456, null=True, unique=True),
        ),
    ]
