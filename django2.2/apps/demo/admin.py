from django.contrib import admin
from .models import TestModel1
# Register your models here.
from utils.basic.admins import guardian, taggit, reversion


@admin.register(TestModel1)
class TestModel1Admin(guardian.GuardianAdmin, taggit.TaggitAdmin, reversion.VersionAdmin):
    ''' 对象权限 '''
    list_display = list_display_links = ('id', 'name')
