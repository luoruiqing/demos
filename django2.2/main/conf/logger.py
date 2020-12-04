import os
from .default import BASE_DIR

LOGGER_PATH = f'{BASE_DIR}/logs'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'class': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(asctime)s [%(levelname)s %(module)s %(process)d %(thread)d] %(message)s',
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'red',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            },
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {  # 默认的
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGER_PATH, "all.log"),
            'maxBytes': 1024 * 1024 * 50,  # 50M
            'backupCount': 3,  # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8'
        },
        'error': {  # 错误日志
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGER_PATH, "error.log"),
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'script': {  # 异步任务或脚本日志
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "script.log"),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'default', 'error'],
            'level': 'INFO',
            'propagate': True
        },
    },
}

os.makedirs(LOGGER_PATH, exist_ok=True)  # 创建日志目录
