import graphene
import graphene_django
import taggit
from apps.demo.models import TestModel1
from django.contrib.auth.models import User as UserModel
from django.contrib.contenttypes.models import ContentType
from graphene.types import generic  # 通用字段
from utils import graphql

from .types import Color


TagQuery = graphql.GrapDjangoModelQuery(taggit.models.Tag)

@graphene_django.converter.convert_django_field.register(taggit.managers.TaggableManager)
def convert_geofield_to_string(field, registry=None):
     return graphene_django.DjangoListField(TagQuery.model_type, description=field.help_text, required=not field.null)


@TagQuery
@graphql.Querier(TestModel1)
@graphql.Querier(UserModel)
@graphql.Querier(ContentType)
class Query:
    ''' 所有查询 '''


@graphql.EnumQuerier(Color)
class Enums:
    ''' 枚举基础类型, 传入参数类 '''


class QuerySet(Query, Enums, graphene.ObjectType):
    ''' 根查询 '''


class MutationSet(graphene.ObjectType):
    ''' 所有修改, 根据情况配置 '''
    MutationUser = graphql.Mutationer(UserModel).Field()
    DeleteUser = graphql.Deleter(UserModel).Field()


schema = graphene.Schema(query=QuerySet, mutation=MutationSet, auto_camelcase=False)
