import math
from json import JSONEncoder
from collections import Iterable
from django.db.models import Model, QuerySet
from django.forms.models import model_to_dict as django_mtd


def model_to_dict(instance, fields=None, exclude=None):
    ''' 模型转字典 '''
    result = {}  # 原类型
    if isinstance(instance, dict):  # 字典类型
        for key, value in instance.items():
            if fields and key not in fields:  # 保留指定字段
                del instance[key]  # 清除
                continue
            if exclude and key in exclude:  # 排除指定字段
                del instance[key]
                continue
            result[key] = model_to_dict(value, fields=fields, exclude=exclude)  # 回调更新
    elif isinstance(instance, (list, Iterable, QuerySet)) and not isinstance(instance, str):  # 除字符类型的任何可迭代对象包含生成器
        result = [model_to_dict(row, fields=fields, exclude=exclude) for row in instance]  # 回调更新
    elif isinstance(instance, Model):
        result = django_mtd(instance, fields=fields, exclude=exclude)
    elif isinstance(result, float) and math.isnan(result):  # 增加nan的兼容逻辑
        result = ''
    return result or instance


mtd = model_to_dict


class DjangoJSONEncoder(JSONEncoder):

    def default(self, o):
        return model_to_dict(o) or super().default(o)
