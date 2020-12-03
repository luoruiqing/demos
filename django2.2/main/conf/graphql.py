from .default import INSTALLED_APPS


INSTALLED_APPS += [
    'graphene_django',  # Graphql
]


GRAPHENE = {
    'SCHEMA': 'main.schema.schema'
}
