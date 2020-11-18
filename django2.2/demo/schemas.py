from graphene.types import generic  # 通用字段
from django.contrib.auth.models import User as UserModel
from django.contrib.contenttypes.models import ContentType
from graphene_django import DjangoObjectType
import graphene
from utils.graphql import Querier, EnumQuerier, Mutationer, Deleter
from .types import Color


@Querier(UserModel)
@Querier(ContentType)
class Query:
    ''' 所有查询 '''


@EnumQuerier(Color)
class Enums:
    ''' 枚举基础类型, 传入参数类 '''


class QuerySet(Query, Enums, graphene.ObjectType):
    ''' 根查询 '''


class MutationSet(graphene.ObjectType):
    ''' 所有修改, 根据情况配置 '''
    MutationUser = Mutationer(UserModel).Field()
    DeleteUser = Deleter(UserModel).Field()


schema = graphene.Schema(query=QuerySet, mutation=MutationSet, auto_camelcase=False)
