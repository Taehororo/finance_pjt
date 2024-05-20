from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)   # articles/articles/
router.register(r'comments', CommentViewSet)   # articles/comments/

app_name = 'articles'
urlpatterns = [
    path('', include(router.urls)),
]