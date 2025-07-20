import pytest
from rest_framework.test import APIClient
from apps.gameplay.models import QuestionCategory


@pytest.mark.django_db
def test_create_category():
    client = APIClient()
    data = {
        "name": "Детство и воспоминания",
        "description": "Ностальгические истории, игры и забавные моменты из детства.",
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
