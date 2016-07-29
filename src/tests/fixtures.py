import pytest

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient


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
def rest_client():
    return APIClient()
