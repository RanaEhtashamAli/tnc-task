import os

from celery import Celery


app = Celery('tnc_task')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'get_exchange_rate': {
        'task': 'tnc_task.exchangerate.tasks.exchange_rate_task',
        'schedule': 60.0
    }
}
