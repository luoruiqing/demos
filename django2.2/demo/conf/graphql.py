from .default import INSTALLED_APPS


INSTALLED_APPS += [
    'graphene_django',  # Graphql
]


GRAPHENE = {
    'SCHEMA': 'demo.schema.schema'
}
