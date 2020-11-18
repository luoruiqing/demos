from .query import GrapDjangoModelQuery
from .enum import GrapEnumQuery
from .mutation import GrapDjangoModelMutation
from .delete import GrapDjangoModelDelete


Querier = GrapDjangoModelQuery
EnumQuerier = GrapEnumQuery
Mutationer = GrapDjangoModelMutation
Deleter = GrapDjangoModelDelete
