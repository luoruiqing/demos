import graphene
from graphene_django import DjangoObjectType
from .base import GrapDjangoModelQueryBase


class GrapDjangoModelQuery(GrapDjangoModelQueryBase):
    ''' 查询基类, 继承实现 executor 即可定制开发 '''

    def executor(self, info, args, **kwargs):
        limit = kwargs.pop('limit', 20)
        page = max(kwargs.pop('page', 1), 1)
        query = self.model.objects.filter(**kwargs.get('filter', {}))
        query = query.exclude(**kwargs.get('exclude', {}))
        if 'order_by' in kwargs:
            query = query.order_by(kwargs['order_by'])
        return self.QueryModel(data=query[page * limit - limit:page * limit], total=query.count())
