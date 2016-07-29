from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.notes.models import Note
from apps.notes.serializers import NoteSerializer
from apps.notes.permissions import IsNoteOwner


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsNoteOwner, )
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(owner=request.user)

