from django.contrib.auth.models import User
from django.db import models

from apps.tags.models import Tag


class Note(models.Model):
    owner = models.ForeignKey(User, related_name="notes")
    tags = models.ManyToManyField(Tag, related_name="notes", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250, blank=True)
    note = models.TextField()

    def __str__(self):
      return self.title
