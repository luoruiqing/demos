from .default import __PARSED_CACHE, INSTALLED_APPS

INSTALLED_APPS += (
    'channels',  # WebSocket
)

ASGI_APPLICATION = "demo.asgi.application"  # ASGI 设置

CHANNEL_LAYERS = {  # WebSocket 依赖
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(__PARSED_CACHE.host, __PARSED_CACHE.port)],
        },
    },
}