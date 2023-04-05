from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'retrieve_social_posts_every_hour': {
        'task': 'traffikboss.tasks.retrieve_social_posts',
        'schedule': crontab(hour='*'),
    },
    'check_app_status_every_30_mins': {
        'task': 'traffikboss.tasks.check_app_status',
        'schedule': crontab(hour='*'),
    }
}