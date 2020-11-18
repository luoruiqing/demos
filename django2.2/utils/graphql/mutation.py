
import graphene
from graphene_django import DjangoObjectType
from .base import GrapDjangoModelMutationBase


class GrapDjangoModelMutation(GrapDjangoModelMutationBase):
    def executor(self, info, args, **kwargs):
        data = kwargs.get('data', {})  # 数据
        pk = data.pop(self.model._meta.pk.name, None)
        # check_conflict(data)  # 处理冲突字段
        created = False
        if pk:  # 有主键则修改
            object_ = self.model.objects.get(pk=pk)
            object_.__dict__.update(**data)
            object_.save()
        else:  # 无主键则创建
            object_ = self.model.objects.create(**data)
            created = True
        return self.MutationModel(**{self.model.__name__: object_, 'status': created})
