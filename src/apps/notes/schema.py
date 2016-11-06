from graphene import relay, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Note


class NoteNode(DjangoObjectType):
    class Meta:
        model = Note
        filter_fields = {
            'owner': ['exact'],
            'title': ['exact', 'icontains'],
            'note': ['exact', 'icontains'],
        }
        filter_order_by = ['created']
        interfaces = (relay.Node, )


class Query(AbstractType):
    note = relay.Node.Field(NoteNode)
    notes = DjangoFilterConnectionField(NoteNode)

    # def resolve_all_notes(self, args, context, info):
        # notes = super(Query, self).resolve_all_notes(args, context, info)
        # import ipdb; ipdb.set_trace()
        # return Note.objects.filter(owner=context.user)
