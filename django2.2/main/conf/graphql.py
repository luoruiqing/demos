from .default import INSTALLED_APPS


INSTALLED_APPS += [
    'graphene_django',  # Graphql
]


GRAPHENE = {
    'SCHEMA': 'main.schema.schema',
    # 'MIDDLEWARE': (
    #    'utils.basic.graphql.middleware.AuthorizationMiddleware',
    # ),
    # 'RELAY_CONNECTION_MAX_LIMIT': 100, # 中转个数
    # 'DJANGO_CHOICE_FIELD_ENUM_V3_NAMING': True, # 全名称
}
