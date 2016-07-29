from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.tags.models import Tag
from apps.tags.serializers import TagSerializer
from apps.tags.permissions import IsTagOwner


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsTagOwner, )
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)
