from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Question, QuestionCategory, Rule
from .serializers import QuestionSerializer, QuestionRequestSerializer, QuestionCategorySerializer, RuleSerializer
from django.db.models.functions import Random
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly


@api_view(['POST'])
def get_random_questions(request):
    serializer = QuestionRequestSerializer(data=request.data)
    if serializer.is_valid():
        question_type = serializer.validated_data['question_type']
        category_ids = serializer.validated_data['category_ids']
        excluded_ids = serializer.validated_data.get('excluded_ids', [])

        queryset = Question.objects.filter(
            question_type=question_type,
            category__id__in=category_ids
        ).exclude(id__in=excluded_ids)

        random_questions = queryset.order_by(Random())[:5]

        serialized = QuestionSerializer(random_questions, many=True)
        return Response(serialized.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class QuestionCategoryViewSet(viewsets.ModelViewSet):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class RuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAdminOrReadOnly]
