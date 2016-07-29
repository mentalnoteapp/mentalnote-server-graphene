from rest_framework import serializers

from apps.notes.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'owner',
            'created',
            'name'
        )
