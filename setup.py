from __future__ import absolute_import
from distutils.core import setup

"""
WangBlog
========

Sentry is a realtime event logging and aggregation platform. It specializes
in monitoring errors and extracting all the information needed to do a proper
post-mortem without any of the hassle of the standard user feedback loop.

WangBlog is a Server
------------------

The Sentry package, at its core, is just a simple server and web UI. It will
handle authentication clients (such as `Raven
<https://github.com/getsentry/raven-python>`_)
and all of the logic behind storage and aggregation.

That said, Sentry is not limited to Python. The primary implementation is in
Python, but it contains a full API for sending events from any language, in
any application.

:copyright: (c) 2011-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

import sys

if sys.version_info[:2] < (2, 7):
    print 'Error: Wangblog requires Python 2.7'
    sys.exit(1)

from distutils.command.build import build as BuildCommand
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist as SDistCommand
from setuptools.command.develop import develop as DevelopCommand
install_requires = []
tests_require = []
dev_requires = []
postgres_requires = []
dsym_requires = []


class WangblogSDistCommand(SDistCommand):
    # If we are not a light build we want to also execute build_js as
    # part of our source build pipeline.
        sub_commands = SDistCommand.sub_commands


class WangblogBuildCommand(BuildCommand):
    def run(self):
        BuildCommand.run(self)


class WangblogDevelopCommand(DevelopCommand):

    def run(self):
        DevelopCommand.run(self)

cmdclass = {
    'sdist': WangblogSDistCommand,
    'build': WangblogBuildCommand,
    'develop': WangblogDevelopCommand,
}

setup(
    name='WangBlog',
    version='1.0',
    # packages=['src.wangblog', 'src.wangblog.web', 'src.wangblog.blog', 'src.wangblog.conf', 'src.wangblog.tests',
    #           'src.wangblog.models', 'src.wangblog.static'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    url='http://www.coolshine.net',
    license='',
    author='wanghe',
    author_email='wangh@loginsight.cn',
    description='Personal website',
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
        'dev': dev_requires,
        'postgres': install_requires + postgres_requires,
        'dsym': dsym_requires,
    },
    entry_points={
        'console_scripts': [
            'wangblog = wangblog.runner:main',
        ],
        'flake8.extension': [
        ],
    },
    cmdclass=cmdclass,
)