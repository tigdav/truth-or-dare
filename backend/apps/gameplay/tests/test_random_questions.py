import pytest
from rest_framework.test import APIClient
from apps.gameplay.models import Question, QuestionCategory


@pytest.mark.django_db
def test_random_questions_selection():
    category = QuestionCategory.objects.create(
        name="Close Circle",
        description="Questions about friends, family, coworkers, and personal boundaries.",
        is_adult=False
    )

    for i in range(10):
        Question.objects.create(
            text=f"Is it true that this is question number {i}?",
            question_type="truth",
            category=category
        )

    client = APIClient()

    request_data = {
        "question_type": "truth",
        "category_ids": [category.id],
        "excluded_ids": []
    }
    response = client.post("/api/questions/random/", request_data, format='json')

    assert response.status_code == 200

    assert len(response.data) <= 5

    for question in response.data:
        assert question["question_type"] == "truth"
        assert question["category_id"] == category.id
        assert "text" in question and question["text"].startswith("Is it true")

    assert all(q["id"] not in request_data["excluded_ids"] for q in response.data)
