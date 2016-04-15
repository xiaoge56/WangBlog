# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: __init__.py.py
time   : 16/4/15 下午9:20  
"""

import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wangblog.conf.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
