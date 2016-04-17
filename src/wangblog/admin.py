# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: admin.py
time   : 16/4/16 下午6:30  
"""

from django.contrib import admin

# Register your models here.
from wangblog.models.user import User
admin.site.register(User)
