"""Celery config file."""
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prodapt.settings')
app = Celery('prodapt')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
