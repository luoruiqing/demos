from .default import DEBUG, INSTALLED_APPS, MIDDLEWARE


if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    # 该中间件放在入口处效果最好
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    INTERNAL_IPS = ['127.0.0.1', 'localhost']
    DEBUG_TOOLBAR_CONFIG = {  # Jquery 地址
        "JQUERY_URL": '//cdn.bootcss.com/jquery/2.2.4/jquery.min.js',
    }
