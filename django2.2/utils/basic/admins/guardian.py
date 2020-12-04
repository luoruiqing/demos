import traceback
from django.db import models
from urllib.parse import unquote
from django.contrib.auth.models import Group
from guardian.core import ObjectPermissionChecker
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_perms, get_objects_for_user, get_objects_for_group, assign_perm, remove_perm, get_users_with_perms, get_groups_with_perms
from django.contrib.contenttypes.admin import GenericTabularInline

ACTIONS = ('view', 'add', 'change', 'delete')


class UserAdminBaseMixin:
    ''' 自定义用户权限扩展基类 '''


class DjangoGuardianAdminMixin(UserAdminBaseMixin):
    ''' django-guardian 权限模块与admin结合 '''
    model_user_field = 'user'  # 用户 - 字段名
    model_group_field = 'group'  # 用户组 - 字段名
    actions = ACTIONS

    @property
    def _perms(self):
        ''' 获取model设置的权限列表 '''
        return (p[0] for p in self.opts.permissions)

    # 列表页面 =====================================================================================

    def get_list_filter(self, request):
        ''' TODO 右侧过滤只能有权限内指定的字段 '''
        return super().get_list_filter(request)

    def get_queryset(self, request):
        ''' 获取可编辑的数据范围 '''
        return get_objects_for_user(user=request.user, klass=super().get_queryset(request), perms=self._perms)

    # 编辑页面 =====================================================================================

    def get_relevance(self, db_field, request, formfield, **kwargs):
        ''' 获取外键的数据相关, 数据A可见, 则数据A.b 也可见'''
        if not request.user.is_superuser:
            formfield.queryset = get_objects_for_user(user=request.user, klass=formfield.queryset, perms=self._perms)  # 获取权限内的外键字段
            try:
                object_id = request.resolver_match.kwargs.get('object_id') or ''  # 获取查询的主键
                if object_id:  # 编辑页面
                    object_id = object_id.replace('_5F', '_')  # Django的 uuid内的下划线会转义
                    obj = self.model.objects.get(pk=unquote(object_id or ''))  # 当前页面主数据
                    pks = getattr(getattr(obj, db_field.name, None), 'pk', None)  # 找到外键数据
                    if isinstance(db_field, models.ForeignKey):
                        pks = [pks]
                    else:
                        pks = [getattr(i, 'pk') for i in getattr(obj, db_field.name).all()]
                    formfield.queryset = formfield.queryset | formfield.queryset.model.objects.filter(pk__in=pks)  # 合并已有权限和有关系的权限数据
            except Exception:
                traceback.print_exc()
                formfield.queryset = formfield.queryset.none()  # 清空连接, 不可选
        return formfield

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        ''' 一对多, 禁止越权选项'''
        return self.get_relevance(db_field, request, super().formfield_for_foreignkey(db_field, request, **kwargs))

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        ''' 多对多, 禁止越权选项 '''
        return self.get_relevance(db_field, request, super().formfield_for_manytomany(db_field, request, **kwargs))

    def get_readonly_fields(self, request, *args, **kwargs):
        ''' 非超级用户不可以直接编辑用户字段 '''
        readonly_fields = super().get_readonly_fields(request, *args, **kwargs)
        if not request.user.is_superuser:
            readonly_fields = (readonly_fields or tuple()) + tuple(
                (f.name for f in self.opts.fields if f.name in (self.model_user_field, self.model_group_field))
            )
        return readonly_fields

    def save_model(self, request, obj, form, change):
        ''' 编辑页保存时刻 '''
        obj.user = request.user  # 最后修改用户为自己
        result = super().save_model(request, obj, form, change)
        for action in self.actions if not request.user.is_superuser and not change else []:
            assign_perm(f'{self.opts.app_label}.{action}_{self.opts.model_name}', request.user, obj)  # 合并用户权限到当前修改人
        return result

    def has_perm(self, request, obj, action):
        ''' 是否有操作权限 '''
        return request.user.has_perm(f'{self.opts.app_label}.{action}_{self.opts.model_name}', obj)

    has_view_permission = lambda self, request, obj=None: self.has_perm(request, obj, 'view')
    has_change_permission = lambda self, request, obj=None: self.has_perm(request, obj, 'change')
    has_delete_permission = lambda self, request, obj=None: self.has_perm(request, obj, 'delete')


class DjangoGuardedPermissionModelAdmin(DjangoGuardianAdminMixin, GuardedModelAdmin):
    ''' django-guardian 组合模型 '''


GuardianAdmin = DjangoGuardedPermissionModelAdmin
