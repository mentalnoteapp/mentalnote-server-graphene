from graphene import relay, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Tag


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = {
            'owner': ['exact'],
            'name': ['exact', 'icontains'],
        }
        filter_order_by = ['created']
        interfaces = (relay.Node, )


class Query(AbstractType):
    tag = relay.Node.Field(TagNode)
    tags = DjangoFilterConnectionField(TagNode)
