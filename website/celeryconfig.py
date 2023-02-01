from celery.schedules import crontab

CELERY_IMPORTS = ('github_check')
#CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'github_check-celery': {
        'task': 'github_check.check_nyt_data',
        'schedule': crontab(hour=19, minute=00,day_of_week="*"),
    }
}
