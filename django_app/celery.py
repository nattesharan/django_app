from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_app.settings')
app = Celery('django_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# command to start celery 
# celery -A django_app worker -l info
#starting celery beat for periodic tasks
# celery -A django_app beat -l info
# to use db for configuring periodic tasks
# celery -A django_app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# celery multi start django_app -A django_app --pidfile="%n.pid" --loglevel=info --logfile='django_app.log'
# celery multi stop django_app -A django_app --pidfile="%n.pid" --loglevel=info --logfile='django_app.log'
# celery multi restart django_app -A django_app --pidfile="%n.pid" --loglevel=info --logfile='django_app.log'


# celery multi start django_app_beat -A django_app --beat -c 1 --pidfile="%n.pid" --loglevel=info logfile="django_beat.log" --scheduler=django_celery_beat.schedulers:DatabaseScheduler
# celery multi stop django_app_beat -A django_app --beat -c 1 --pidfile="%n.pid" --loglevel=info logfile="django_beat.log" --scheduler=django_celery_beat.schedulers:DatabaseScheduler
# celery multi restart django_app_beat -A django_app --beat -c 1 --pidfile="%n.pid" --loglevel=info logfile="django_beat.log" --scheduler=django_celery_beat.schedulers:DatabaseScheduler