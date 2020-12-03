import graphene
from django.contrib.auth.models import User as UserModel
from django.contrib.contenttypes.models import ContentType
from graphene.types import generic  # 通用字段
from graphene_django import DjangoObjectType
from utils import graphql

from .types import Color


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
