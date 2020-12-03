from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from taggit.managers import TaggableManager


class TestModel1(models.Model):
    """ 测试表 """
    name = models.CharField(_("name"), max_length=255, help_text="名称")
    tags = TaggableManager()

    class Meta:
        verbose_name = verbose_name_plural = '测试表 1'
