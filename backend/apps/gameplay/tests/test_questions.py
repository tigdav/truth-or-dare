import pytest
from rest_framework.test import APIClient
from apps.gameplay.models import Question, QuestionCategory


@pytest.mark.django_db
def test_create_dare_question_in_strange_habits_category():
    category = QuestionCategory.objects.create(
        id=6,
        name="Странные привычки",
        description="Необычные ритуалы, повседневные причуды и личные особенности.",
        is_adult=False
    )

    client = APIClient()
    data = {
        "text": "Сделай 10 приседаний, повторяя своё любимое странное слово.",
        "question_type": "dare",
        "category": category.id
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
