import pytest
from rest_framework.test import APIClient
from apps.gameplay.models import Question, QuestionCategory


@pytest.mark.django_db
def test_random_questions_selection():
    category = QuestionCategory.objects.create(
        name="Close Circle",
        description="Questions about friends, family, coworkers, and personal boundaries.",
        is_adult=False,
    )

    for i in range(10):
        Question.objects.create(
            text=f"Is it true that this is question number {i}?", question_type="truth", category=category
        )

    client = APIClient()

    request_data = {"question_type": "truth", "category_ids": [category.id], "excluded_ids": []}
    response = client.post("/api/questions/random/", request_data, format="json")

    assert response.status_code == 200

    assert len(response.data) <= 5

    for question in response.data:
        assert question["question_type"] == "truth"
        assert question["category_id"] == category.id
        assert "text" in question and question["text"].startswith("Is it true")

    assert all(q["id"] not in request_data["excluded_ids"] for q in response.data)


@pytest.mark.django_db
def test_random_questions_excludes_specified_ids():
    category = QuestionCategory.objects.create(
        name="Mixed", description="Holds multiple truth questions.", is_adult=False
    )
    questions = [
        Question.objects.create(text=f"Truth statement {i}?", question_type="truth", category=category)
        for i in range(8)
    ]
    excluded = [questions[0].id, questions[1].id, questions[2].id]

    client = APIClient()
    request_data = {
        "question_type": "truth",
        "category_ids": [category.id],
        "excluded_ids": excluded,
    }
    response = client.post("/api/questions/random/", request_data, format="json")

    assert response.status_code == 200
    returned_ids = [q["id"] for q in response.data]
    assert all(qid not in excluded for qid in returned_ids)


@pytest.mark.django_db
def test_random_questions_filters_by_type():
    category = QuestionCategory.objects.create(
        name="Mixed Types", description="Has both truth and dare questions.", is_adult=False
    )
    for i in range(5):
        Question.objects.create(text=f"Truth {i}", question_type="truth", category=category)
    for i in range(5):
        Question.objects.create(text=f"Dare {i}", question_type="dare", category=category)

    client = APIClient()
    request_data = {
        "question_type": "dare",
        "category_ids": [category.id],
    }
    response = client.post("/api/questions/random/", request_data, format="json")

    assert response.status_code == 200
    assert len(response.data) > 0
    for q in response.data:
        assert q["question_type"] == "dare"


@pytest.mark.django_db
def test_random_questions_returns_empty_when_no_match():
    category = QuestionCategory.objects.create(
        name="Truth Only", description="Only truth questions exist here.", is_adult=False
    )
    Question.objects.create(text="Only truth here.", question_type="truth", category=category)

    client = APIClient()
    request_data = {
        "question_type": "dare",
        "category_ids": [category.id],
    }
    response = client.post("/api/questions/random/", request_data, format="json")

    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_random_questions_invalid_type_returns_400():
    category = QuestionCategory.objects.create(
        name="Validation", description="Used for validation testing.", is_adult=False
    )

    client = APIClient()
    request_data = {
        "question_type": "invalid",
        "category_ids": [category.id],
    }
    response = client.post("/api/questions/random/", request_data, format="json")

    assert response.status_code == 400
    assert "question_type" in response.data


@pytest.mark.django_db
def test_random_questions_empty_categories_returns_400():
    client = APIClient()
    request_data = {
        "question_type": "truth",
        "category_ids": [],
    }
    response = client.post("/api/questions/random/", request_data, format="json")

    assert response.status_code == 400
    assert "category_ids" in response.data
