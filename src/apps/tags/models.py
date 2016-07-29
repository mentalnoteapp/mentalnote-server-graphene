from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    owner = models.ForeignKey(User, related_name="tags")
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
