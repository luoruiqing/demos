from .default import DEBUG, INSTALLED_APPS, MIDDLEWARE


if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INTERNAL_IPS = ['127.0.0.1', 'localhost']
    DEBUG_TOOLBAR_CONFIG = {  # Jquery 地址
        "JQUERY_URL": '//cdn.bootcss.com/jquery/2.2.4/jquery.min.js',
    }
