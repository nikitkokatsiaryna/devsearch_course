import os
from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')

app = Celery('devsearch', broker='pyamqp://guest@localhost//')


# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()


@app.task
def add(x, y):
    return (x + y)


add.delay(6,6)
