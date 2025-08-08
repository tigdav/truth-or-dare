from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Question, QuestionCategory, Rule
from .serializers import QuestionSerializer, QuestionRequestSerializer, QuestionCategorySerializer, RuleSerializer
from django.db.models.functions import Random
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsAdminOrReadOnly


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

    @action(
        detail=False,
        methods=['post'],
        url_path='random',
        permission_classes=[AllowAny]
    )
    def get_random_questions(self, request):
        req_serializer = QuestionRequestSerializer(data=request.data)
        req_serializer.is_valid(raise_exception=True)

        question_type = req_serializer.validated_data['question_type']
        category_ids = req_serializer.validated_data['category_ids']
        excluded_ids = req_serializer.validated_data.get('excluded_ids', [])

        queryset = Question.objects.filter(
            question_type=question_type,
            category__id__in=category_ids
        ).exclude(id__in=excluded_ids)

        random_questions = queryset.order_by(Random())[:5]

        serializer = QuestionSerializer(random_questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionCategoryViewSet(viewsets.ModelViewSet):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class RuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
    permission_classes = [IsAdminOrReadOnly]
