from .default import INSTALLED_APPS


INSTALLED_APPS.insert(
    INSTALLED_APPS.index('django.contrib.admin'),
    'admin_menu'
)
