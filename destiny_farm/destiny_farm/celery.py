import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'destiny_farm.settings')

app = Celery('destiny_farm')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

