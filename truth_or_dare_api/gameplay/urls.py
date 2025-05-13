from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, QuestionCategoryViewSet
from .views import get_random_questions

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'categories', QuestionCategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/questions/random/', get_random_questions, name='get_random_questions'),
]
