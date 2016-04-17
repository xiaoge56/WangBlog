# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: init.py
time   : 16/4/16 下午9:57  
"""
# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

from django.core.management.base import BaseCommand, CommandError
from oauth2_provider.models import Application
from django.conf import settings



def update_sentry_instances():
    """
    update sentry instance model from remoting aliyun ecs
    """
    pass


# create sentry oauth application record
def create_sentry_application():
    name = 'loginsight saas'
    client_id = settings.DEFALUT_SENTRY_CLIENT_ID
    client_secret = settings.DEFAULT_SENTRY_CLIENT_SECRET
    authorization_grant_type = Application.GRANT_AUTHORIZATION_CODE
    client_type = Application.CLIENT_PUBLIC
    if settings.DEBUG:
        redirect_url = "http://localhost/oauth/consumer/exchange/"
    else:
        redirect_url = "http://app.loginsight.cn/oauth/consumer/exchange/"

    if not Application.objects.filter(name=name):
        Application.objects.create(name=name,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   authorization_grant_type=authorization_grant_type,
                                   client_type=client_type,
                                   redirect_uris=redirect_url,
                                   user_id=1)
        return client_id, client_secret


def create_logagent_application():
    if not Application.objects.filter(client_id=settings.LOGAGENT_CLIENT_ID):
        Application.objects.create(name="logagent",
                                   client_id=settings.LOGAGENT_CLIENT_ID,
                                   client_secret=settings.LOGAGENT_CLIENT_SECRET,
                                   authorization_grant_type=Application.GRANT_PASSWORD,
                                   client_type= Application.CLIENT_CONFIDENTIAL,
                                   redirect_uris='',
                                   user_id=1)



class Command(BaseCommand):
    def handle(self, *args, **options):
        # 创建一个oauth provider application 给logagent
        # 更新实例数据表
        print('Initilize website ...')
        create_sentry_application()
        create_logagent_application()
