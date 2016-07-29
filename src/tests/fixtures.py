import pytest

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient

from apps.notes.models import Note
from apps.tags.models import Tag


@pytest.fixture
def rest_client():
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def user():
    user =  User.objects.create(
        username='testuser',
        password='123'
    )
    return user


@pytest.fixture
@pytest.mark.django_db
def note(user):
    note = Note.objects.create(
        owner=user,
        title='test note',
        note='test note body'
    )
    return note


@pytest.fixture
@pytest.mark.django_db
def note(user):
    note, created = Note.objects.get_or_create(
        owner=user,
        title='test note',
        note='test note body'
    )
    return note


@pytest.fixture
@pytest.mark.django_db
def tag(user):
    tag, created = Tag.objects.get_or_create(
        owner=user,
        name='test tag'
    )
    return tag
