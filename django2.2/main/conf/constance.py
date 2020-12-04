from .default import INSTALLED_APPS
# https://django-constance.readthedocs.io/ 用于动态配置


INSTALLED_APPS += [
    'constance',
    'constance.backends.database',
]

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_DATABASE_CACHE_BACKEND = 'default'  # 采用默认缓存加速
CONSTANCE_DATABASE_CACHE_AUTOFILL_TIMEOUT = None  # Redis 未启动则忽略

# CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True


CONSTANCE_CONFIG = {
    'THE_ANSWER': (42, 'Answer to the Ultimate Question of Life, '
                       'The Universe, and Everything'),
}
