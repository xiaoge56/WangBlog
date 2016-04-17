# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: user.py
time   : 16/4/17 上午9:06  
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'organization_name', 'phone', 'is_staff',)

