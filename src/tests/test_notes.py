import pytest

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient

from apps.notes.models import Note


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


def test_notes_list_GET_401(rest_client):
    """
    no unauthorized access
    """
    url = reverse('notes-list')
    response = rest_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_notes_list_GET_200(rest_client, user, note):
    """
    note owner can access notes collection
    """

    rest_client.force_authenticate(user=user)
    url = reverse('notes-list')
    response = rest_client.get(url)

    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_notes_detail_GET_401(rest_client, note):
    """
    no unauthorized access
    """

    url = reverse('notes-detail', kwargs={"pk": note.id})
    response = rest_client.get(url)

    assert response.status_code == 401


@pytest.mark.django_db
def test_notes_detail_GET_200(rest_client, user, note):
    """
    note owner can access note detail
    """

    rest_client.force_authenticate(user=user)
    url = reverse('notes-detail', kwargs={"pk": note.id})
    response = rest_client.get(url)

    assert response.status_code == 200
    assert len(response.data) > 0
