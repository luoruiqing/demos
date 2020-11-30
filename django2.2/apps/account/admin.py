from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from .models import User


@admin.register(User)
class UserAdmin(UserAdminBase):
    ''' 用户视图 '''
    # fieldsets = UserAdminBase.fieldsets + (
    #     (_('用户信息'), {'fields': ()}),
    # )
