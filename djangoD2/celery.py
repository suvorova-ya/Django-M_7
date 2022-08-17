import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoD2.settings')

app = Celery('djangoD2')
app.config_from_object('django.conf:settings', namespace='CELERY')



#
# app.conf.beat_schedule = {
#     'notify_post_create': {
#         'task': 'news_portal.tasks.notify_post_create',
#         'schedule': crontab(),
#
#     }
# }


app.conf.beat_schedule = {
    'weekly_mail_8am': {
        'task': 'news_portal.tasks.weekly_mailing_list',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),

    }
}
app.autodiscover_tasks()