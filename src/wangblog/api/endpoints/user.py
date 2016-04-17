# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: user.py
time   : 16/4/17 上午9:06  
"""
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from wangblog.api.serializers.user import UserSerializer
from django.shortcuts import get_object_or_404


from django.contrib.auth import get_user_model
User = get_user_model()


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(APIView):
    permission_classes = ()

    def get(self, request,  *args, **kwargs):
        data = {
            'username': request.user.username,
            'organization_name': request.user.organization_name,
            'id': request.user.id
        }
        return Response(data=data, status=200)

