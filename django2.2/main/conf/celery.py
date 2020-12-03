import djcelery
from celery.schedules import crontab
from .default import INSTALLED_APPS, CACHE_URL, TIME_ZONE

# https://kinegratii.github.io/2015/10/22/djcelery-practice/

CELERY_TIMEZONE = TIME_ZONE  # 任务时区
BROKER_URL = CACHE_URL
# CELERY_IMPORTS = ('.my_celery.tasks', ) # 任务定义所在的模块

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

INSTALLED_APPS += (
    'djcelery',  # 加入djcelery应用
)


CELERYBEAT_SCHEDULE = {  # 启动时自动写入库中
    '定时清除孤儿对象权限': {
        'task': 'account.tasks.clean_orphan_obj_perms',
        'schedule': crontab(minute=0, hour=0),
        "args": ()
    },
}

djcelery.setup_loader()
