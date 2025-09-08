import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.gameplay.models import Question, QuestionCategory


@pytest.mark.django_db
def test_create_dare_question_in_strange_habits_category():
    category = QuestionCategory.objects.create(
        id=6,
        name="Unusual Habits",
        description="Quirky rituals, everyday oddities, and personal peculiarities.",
        is_adult=False
    )

    User.objects.create_user(username='admin', password='adminpass', is_staff=True)

    client = APIClient()
    client.login(username='admin', password='adminpass')

    data = {
        "text": "Do 10 squats while repeating your favorite weird word.",
        "question_type": "dare",
        "category_id": category.id
    }

    response = client.post("/api/questions/", data, format='json')

    assert response.status_code == 201

    assert Question.objects.count() == 1

    question = Question.objects.first()

    assert question.text == data["text"]
    assert question.question_type == data["question_type"]
    assert question.category_id == category.id

    assert "id" in response.data
    assert response.data["text"] == data["text"]
