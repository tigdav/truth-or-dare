from rest_framework import serializers
from .models import Question, QuestionCategory, Rule


class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = ['id', 'name', 'description', 'icon', 'is_adult']


class QuestionSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=QuestionCategory.objects.all(),
        required=True
    )

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'category_id']


class QuestionRequestSerializer(serializers.Serializer):
    question_type = serializers.ChoiceField(choices=['truth', 'dare'])
    category_ids = serializers.ListField(
        child=serializers.IntegerField(), allow_empty=False
    )
    excluded_ids = serializers.ListField(
        child=serializers.IntegerField(), required=False
    )


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ['text']
