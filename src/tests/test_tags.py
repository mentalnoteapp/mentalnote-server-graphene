import pytest

from django.core.urlresolvers import reverse

from .fixtures import rest_client, tag, user


def test_tags_tags_GET_401(rest_client):
    """
    no unauthorized access
    """
    url = reverse('tags-list')
    response = rest_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_tags_list_GET_200(rest_client, user, tag):
    """
    owner can access tags collection
    """

    rest_client.force_authenticate(user=user)
    url = reverse('tags-list')
    response = rest_client.get(url)

    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_tags_list_POST_201(rest_client, user, tag):
    """
    tag owner can post new tag
    """

    rest_client.force_authenticate(user=user)
    url = reverse('tags-list')

    data = {}
    data['owner'] = user.id
    data['name'] = 'one'

    response = rest_client.post(url, data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_tags_detail_GET_401(rest_client, tag):
    """
    no unauthorized access
    """

    url = reverse('tags-detail', kwargs={"pk": tag.id})
    response = rest_client.get(url)

    assert response.status_code == 401


@pytest.mark.django_db
def test_tags_detail_GET_200(rest_client, user, tag):
    """
    tag owner can access tag detail
    """

    rest_client.force_authenticate(user=user)
    url = reverse('tags-detail', kwargs={"pk": tag.id})
    response = rest_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_tags_detail_PUT_200(rest_client, user, tag):
    """
    tag owner can alter tag
    """

    rest_client.force_authenticate(user=user)
    url = reverse('tags-detail', kwargs={"pk": tag.id})

    new_name = 'new tag name'
    data = {}
    data['owner'] = tag.owner.id
    data['name'] = new_name

    response = rest_client.put(url, data)

    assert response.status_code == 200
    assert response.data['name'] == new_name


@pytest.mark.django_db
def test_tags_detail_DELETE_204(rest_client, user, tag):
    """
    tag owner can delete tag
    """

    rest_client.force_authenticate(user=user)
    url = reverse('tags-detail', kwargs={"pk": tag.id})

    response = rest_client.delete(url)

    assert response.status_code == 204
