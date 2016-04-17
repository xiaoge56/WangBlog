# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: upgrade.py
time   : 16/4/16 下午9:54  
"""

"""
sentry.runner.commands.upgrade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2015 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
import click


@click.command()
@click.option('--verbosity', '-v', default=1, help='Verbosity level.')
@click.option('--traceback', default=True, is_flag=True, help='Raise on exception.')
@click.option('--noinput', default=False, is_flag=True, help='Do not prompt the user for input of any kind.')
@click.pass_context
def upgrade(ctx, verbosity, traceback, noinput):
    "Perform any pending database migrations and upgrades."

    from django.core.management import call_command as dj_call_command
    dj_call_command(
        'syncdb',
        interactive=not noinput,
        traceback=traceback,
        verbosity=verbosity,
    )

    dj_call_command(
        'migrate',
        merge=True,
        ignore_ghost_migrations=True,
        interactive=not noinput,
        traceback=traceback,
        verbosity=verbosity,
    )
