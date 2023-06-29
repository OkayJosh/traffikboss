# myproject/celery.py
import os

from celery import Celery
from django.utils import timezone
from celery.signals import task_prerun, task_postrun
import logging

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traffikboss.settings')


app = Celery('traffikboss')


# Load the celery settings from the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

LOG = logging.getLogger(__name__)


@task_prerun.connect()
def log_task_start(task_id, task, **kwargs):
    LOG.info(f'Started task {task.name} at {timezone.now()}')


@task_postrun.connect()
def log_task_end(task_id, task, **kwargs):
    LOG.info(f'Finished task {task.name} at {timezone.now()}')
