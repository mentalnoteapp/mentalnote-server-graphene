import pytest

from django.core.urlresolvers import reverse

from apps.tags.models import Tag
from .fixtures import note, rest_client, user


@pytest.fixture
@pytest.mark.django_db
def tag(user):
    tag = Tag.objects.create(
        owner=user,
        name='test tag'
    )
    return tag


def test_notes_tags_GET_401(rest_client):
    """
    no unauthorized access
    """
    url = reverse('tags-list')
    response = rest_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_tags_list_GET_200(rest_client, user, tag):
    """
    note owner can access tags collection
    """

    rest_client.force_authenticate(user=user)
    url = reverse('tags-list')
    response = rest_client.get(url)

    assert response.status_code == 200
    assert len(response.data) > 0
