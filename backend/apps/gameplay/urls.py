from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, QuestionCategoryViewSet, RuleViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'categories', QuestionCategoryViewSet)
router.register(r'rules', RuleViewSet, basename='rules')

urlpatterns = [
    path('', include(router.urls)),
]
