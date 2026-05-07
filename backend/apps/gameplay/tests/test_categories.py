import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.gameplay.models import QuestionCategory


@pytest.mark.django_db
def test_create_category():
    User.objects.create_user(username='admin', password='adminpass', is_staff=True)
    client = APIClient()
    client.login(username='admin', password='adminpass')

    data = {
        "name": "Childhood & Memories",
        "description": "Nostalgic stories, games, and funny moments from the past.",
        "is_adult": False
    }

    response = client.post("/api/categories/", data, format='json')

    assert response.status_code == 201

    assert QuestionCategory.objects.count() == 1

    category = QuestionCategory.objects.first()

    assert category.name == data["name"]
    assert category.description == data["description"]
    assert category.is_adult == data["is_adult"]

    assert "id" in response.data
    assert response.data["name"] == data["name"]
    assert response.data["description"] == data["description"]
    assert response.data["is_adult"] == data["is_adult"]


@pytest.mark.django_db
def test_anonymous_can_list_categories():
    QuestionCategory.objects.create(
        name="Public Category",
        description="Listed for anonymous clients.",
        is_adult=False
    )
    client = APIClient()

    response = client.get("/api/categories/")

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_anonymous_can_retrieve_category():
    category = QuestionCategory.objects.create(
        name="Retrievable",
        description="Detail view is public.",
        is_adult=False
    )
    client = APIClient()

    response = client.get(f"/api/categories/{category.id}/")

    assert response.status_code == 200
    assert response.data["name"] == "Retrievable"


@pytest.mark.django_db
def test_non_admin_cannot_create_category():
    User.objects.create_user(username='alice', password='alicepass')
    client = APIClient()
    client.login(username='alice', password='alicepass')

    data = {
        "name": "Forbidden",
        "description": "Should not be created by a non-admin user.",
        "is_adult": False
    }
    response = client.post("/api/categories/", data, format='json')

    assert response.status_code == 403
    assert QuestionCategory.objects.count() == 0


@pytest.mark.django_db
def test_admin_can_update_category():
    category = QuestionCategory.objects.create(
        name="Original",
        description="Before update.",
        is_adult=False
    )

    User.objects.create_user(username='admin', password='adminpass', is_staff=True)
    client = APIClient()
    client.login(username='admin', password='adminpass')

    data = {
        "name": "Updated",
        "description": "After update.",
        "is_adult": True
    }
    response = client.put(f"/api/categories/{category.id}/", data, format='json')

    assert response.status_code == 200

    category.refresh_from_db()
    assert category.name == "Updated"
    assert category.is_adult is True
