from celery import task
from guardian.utils import clean_orphan_obj_perms

# 用于定期删除孤儿对象许可
task(bind=True)(clean_orphan_obj_perms)
