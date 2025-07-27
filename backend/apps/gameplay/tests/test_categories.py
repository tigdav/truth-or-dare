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
