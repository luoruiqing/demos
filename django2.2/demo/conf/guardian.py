from .default import INSTALLED_APPS
# 安装 APP
INSTALLED_APPS += [
    'guardian',
]
# 设置通用用户名称及 ID
ANONYMOUS_USER_NAME = 'AnonymousUser'
ANONYMOUS_USER_ID = -1
# 指定认证的模块有那些
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Django
    'guardian.backends.ObjectPermissionBackend',
)
