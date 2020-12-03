from .default import INSTALLED_APPS
# 安装 APP
INSTALLED_APPS += [
    'guardian',
]
# 设置通用用户名称及 ID
ANONYMOUS_USER_NAME = 'AnonymousUser'
ANONYMOUS_USER_ID = -1

AUTH_USER_MODEL = 'account.User'  # 指定用户模块位置

# 指定认证的模块有那些
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Django
    'guardian.backends.ObjectPermissionBackend',
)

# 可能遇到的问题 --------------------------------------------------------
# 第一次迁移: 创建索引时遇到长度问题
# ALTER TABLE `guardian_userobjectpermission` ROW_FORMAT=DYNAMIC;
# ALTER TABLE `guardian_groupobjectpermission` ROW_FORMAT=DYNAMIC;
# 第二次迁移: 表已经存在, ./manage.py migrate guardian --fake-initial  根据迁移文件, 增加索引
# alter table guardian_userobjectpermission add unique index(`user_id`, `permission_id`, `object_pk`);
# alter table guardian_groupobjectpermission add unique index(`group_id`, `permission_id`, `object_pk`);
