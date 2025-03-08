from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, QuestionCategoryViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'categories', QuestionCategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
