import graphene
from graphene.types import generic  # 通用字段
from graphene_django import DjangoObjectType
from django.utils.functional import cached_property


class GrapBase:
    def executor(self, info, args, **kwargs):
        ''' 执行程序 '''
        raise NotImplementedError()


class GrapDjangoModelEnumBase(GrapBase):
    ''' 类型查询 '''

    def __init__(self, cls):
        self.name = cls.__name__
        self.attrs = {k: getattr(cls, k) for k in dir(cls) if not k.startswith('_')}
        self.model_type = type(f'{self.name}EnumType', (generic.GenericScalar,), {'Meta': type('Meta', (), {})})

    def __call__(self, cls):
        setattr(cls, f'{self.name}Type', graphene.Field(self.model_type))  # 安装
        setattr(cls, f'resolve_{self.name}Type', self.executor)  # 查询方法
        return cls


class GrapDjangoModel(GrapBase):
    ''' Django Model 基础 '''
    MODEL_TYPES = {}

    def __init__(self, model):
        self.model = model
        if model not in self.MODEL_TYPES:  # 处理Type共享
            self.MODEL_TYPES[model] = type(f'{model.__name__}Type', (DjangoObjectType,), {'Meta': type('Meta', (), dict(model=model))})
        self.model_type = self.MODEL_TYPES[model]


class GrapDjangoModelQueryBase(GrapDjangoModel):
    ''' Django Model 查询基础 '''

    @cached_property
    def QueryModel(self):
        return type(f'{self.model.__name__}', (graphene.ObjectType,), {
            'Meta': type('Meta', (), {"description": self.model.__doc__ or ''}),  # 创建meta类
            "data": graphene.List(self.model_type),
            "total": graphene.Int(description="数据条数")
        })

    @cached_property
    def params(self):
        return {
            'limit': graphene.Int(description="条数[20]"),
            'page': graphene.Int(description="页数"),
            'filter': generic.GenericScalar(description="Django Model filters 查询参数"),
            'exclude': generic.GenericScalar(description="Django Model exclude 查询参数"),
            'order_by': generic.GenericScalar(description="Django Model order_by 查询参数, 列表或字符"),
        }

    def __call__(self, cls):
        setattr(cls, self.model.__name__, graphene.Field(self.QueryModel, self.params))  # 安装
        setattr(cls, f'resolve_{self.model.__name__}', self.executor)  # 查询方法
        return cls


class GrapDjangoModelMutationBase(GrapDjangoModel):
    ''' Django Model 修改基础 '''
    FLAG = 'Mutation'

    @cached_property
    def MutationModel(self):
        return type(f'{self.FLAG}{self.model.__name__}', (graphene.Mutation, ), {
            'Arguments': type('Arguments', (), {'data': generic.GenericScalar()}),
            f'{self.model.__name__}': graphene.Field(self.model_type),
            'status': graphene.Boolean(description='状态'),
            'mutate': self.executor,
        })

    def Field(self):
        return self.MutationModel.Field()


class GrapDjangoModelDeleteBase(GrapDjangoModelMutationBase):
    ''' Django Model 删除基础 '''

    FLAG = 'Delete'
