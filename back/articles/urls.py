from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'', ArticleViewSet)   # articles/ 경로에 맞추기 위해 빈 문자열 사용

app_name = 'articles'
urlpatterns = [
    path('', include(router.urls)),
]