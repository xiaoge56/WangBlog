# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: home.py
time   : 16/4/16 下午7:33  
"""
from django.views.generic.base import TemplateView
from django.conf import settings
from oauth2_provider.compat import urlencode


class HomeView(TemplateView):
    template_name = "loginsight/home.html"

    def get_context_data(self, **kwargs):

        kwargs['CLIENT_ID'] = urlencode({'client_id': settings.DEFALUT_SENTRY_CLIENT_ID})
        kwargs['OAUTH_SERVER'] = settings.OAUTH_SERVER
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
