import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studRegSys.settings')
app = Celery('studRegSys')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every': {
        'task': 'anket_app.tasks.update_course',
        'schedule': 60.0,
    }
}
