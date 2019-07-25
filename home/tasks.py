from celery.decorators import periodic_task, task
from datetime import timedelta

@task(name="add")
def add(a, b):
    print(a)
    print(b)

# http://docs.celeryproject.org/en/2.0-archived/getting-started/periodic-tasks.html
@periodic_task(run_every=timedelta(seconds=15),name="test",ignore_result=True)
def cron_func():
    print("HEyyyyyyyy")