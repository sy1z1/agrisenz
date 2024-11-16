from __future__ import absolute_import
import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrisenz.settings')

app = Celery('agrisenz')

# Using a string here means the worker doesn’t have to serialize
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in each app
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
