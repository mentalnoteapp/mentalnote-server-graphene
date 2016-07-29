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
def test_notes_list_POST_201(rest_client, user, note):
    """
    note owner can post new note
    """

    rest_client.force_authenticate(user=user)
    url = reverse('notes-list')

    data = {}
    data['owner'] = user.id
    data['title'] = 'one'
    data['note'] = 'two'
    data['tags'] = []

    response = rest_client.post(url, data)

    assert response.status_code == 201


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


@pytest.mark.django_db
def test_notes_detail_PUT_200(rest_client, user, note):
    """
    note owner can alter note
    """

    rest_client.force_authenticate(user=user)
    url = reverse('notes-detail', kwargs={"pk": note.id})

    new_body = 'new'
    data = {}
    data['owner'] = note.owner.id
    data['title'] = note.title
    data['note'] = new_body

    response = rest_client.put(url, data)

    assert response.status_code == 200
    assert response.data['note'] == new_body


@pytest.mark.django_db
def test_notes_detail_DELETE_204(rest_client, user, note):
    """
    note owner can delete note
    """

    rest_client.force_authenticate(user=user)
    url = reverse('notes-detail', kwargs={"pk": note.id})

    response = rest_client.delete(url)

    assert response.status_code == 204
