import graphene
from graphene_django import DjangoObjectType
from .base import GrapDjangoModelDeleteBase


class GrapDjangoModelDelete(GrapDjangoModelDeleteBase):
    def executor(self, info, args, **kwargs):
        pk = kwargs.get('data', {}).pop(self.model._meta.pk.name, None)
        assert pk, '缺少关键标识!'
        object_ = self.model.objects.get(pk=pk)
        # 源对象删除后不可被解析
        return_object = self.model(**{k: v for k, v in object_.__dict__.items() if k != '_state'})
        return self.MutationModel(**{self.model.__name__: return_object, 'status': object_.delete()})
