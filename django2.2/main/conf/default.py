from .base import *
from sqlalchemy.engine.url import _parse_rfc1738_args


LANGUAGE_CODE = 'zh-hans'  # 语言设置
TIME_ZONE = 'Asia/Shanghai'  # 时区设置

INSTALLED_APPS += [

]


MIDDLEWARE += [
    'utils.basic.middlewares.api.APIMiddleware',
]


# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHE_URL = 'redis://127.0.0.1:6379/0'

# ==============================================================================

try:
    from ..local_setttings import *  # 动态导入配置文件
except ModuleNotFoundError as e:
    pass


__PARSED_CACHE = _parse_rfc1738_args(CACHE_URL)


CACHES = {  # django-redis 依赖
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{__PARSED_CACHE.host}:{__PARSED_CACHE.port}/{__PARSED_CACHE.database}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # 连接超时 秒
            "SOCKET_TIMEOUT": 5,  # 读取超时
            # "IGNORE_EXCEPTIONS": True,  # 忽略连接异常
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",  # 压缩
            #  "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor", # lzma 压缩
        }
    }
}
