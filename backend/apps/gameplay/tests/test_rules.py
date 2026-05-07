import pytest
from rest_framework.test import APIClient

from apps.gameplay.models import Rule


@pytest.mark.django_db
def test_anonymous_can_list_rules():
    Rule.objects.create(text="Rule one.", order=0)
    Rule.objects.create(text="Rule two.", order=1)

    client = APIClient()
    response = client.get("/api/rules/")

    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_rule_response_only_contains_text_field():
    Rule.objects.create(text="Some rule.", order=0)

    client = APIClient()
    response = client.get("/api/rules/")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert set(response.data[0].keys()) == {"text"}


@pytest.mark.django_db
def test_rules_listed_in_order_field():
    Rule.objects.create(text="Third", order=3)
    Rule.objects.create(text="First", order=1)
    Rule.objects.create(text="Second", order=2)

    client = APIClient()
    response = client.get("/api/rules/")

    assert response.status_code == 200
    texts = [rule["text"] for rule in response.data]
    assert texts == ["First", "Second", "Third"]


@pytest.mark.django_db
def test_rules_endpoint_does_not_allow_write():
    client = APIClient()
    response = client.post("/api/rules/", {"text": "Should not work"}, format='json')

    assert response.status_code == 405
