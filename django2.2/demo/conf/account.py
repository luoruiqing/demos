from .default import INSTALLED_APPS

INSTALLED_APPS += [
    'apps.account',
]


AUTH_USER_MODEL = 'account.User'
