# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: auth_login.py
time   : 16/4/16 下午3:59  
"""
from django.conf import settings
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic import View
from wangblog.models.user import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout
from wangblog.web.forms.accounts import AuthenticationForm, RegistrationForm


class RegisterView(View):

    @staticmethod
    def check_phone(request):
        print request.method
        p = request.POST.get('cellphone')
        v = User.objects.filter(phone=p)
        if len(v) == 0:
            return HttpResponse(True)
        else:
            return HttpResponse(False)

    @staticmethod
    def check_email(request):
        if request.method == 'GET':
            e = request.GET.get('email')
        if request.method == 'POST':
            e = request.POST.get('email')
        v = User.objects.filter(email=e)
        if len(v) == 0:
            return HttpResponse(True)
        else:
            return HttpResponse(False)

    @staticmethod
    def check_sub_domain(request):
        pass

    def check_org_name(request):
        if request.method == 'GET':
            org = request.GET.get('org_name')
        v = User.objects.filter('organization_name')
        if len(v) == 0:
            return HttpResponse(True)
        else:
            return HttpResponse(False)

    def get(self, request):
        return render_to_response("loginsight/register.html")


class AccountsRegisterView(RedirectView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass