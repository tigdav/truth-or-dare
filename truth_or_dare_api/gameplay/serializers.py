from rest_framework import serializers
from .models import Question, QuestionCategory


class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = ['id', 'name', 'description', 'is_adult']


class QuestionSerializer(serializers.ModelSerializer):
    category = QuestionCategorySerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'category']
