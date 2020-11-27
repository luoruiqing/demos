import djcelery
from .default import INSTALLED_APPS, CACHE_URL, TIME_ZONE

CELERY_TIMEZONE = TIME_ZONE
BROKER_URL = CACHE_URL
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

INSTALLED_APPS += (
    'djcelery',  # 加入djcelery应用
)


djcelery.setup_loader()
