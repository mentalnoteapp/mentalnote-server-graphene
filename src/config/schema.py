import graphene

import apps.notes.schema
import apps.tags.schema


class Query(apps.notes.schema.Query, apps.tags.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
