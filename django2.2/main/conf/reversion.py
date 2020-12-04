from .default import INSTALLED_APPS

INSTALLED_APPS += [
    'reversion',  # 历史回滚
    'reversion_compare',  # 历史对比
]


# Add reversion models to admin interface:
ADD_REVERSION_ADMIN = True
# optional settings:
REVERSION_COMPARE_FOREIGN_OBJECTS_AS_ID = False
REVERSION_COMPARE_IGNORE_NOT_REGISTERED = False
