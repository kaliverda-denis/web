from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
# ДОДАНО: Роутер для reviews
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # ВИПРАВЛЕНО: Видалено path('books/create/', ...) — дублікат функціоналу BookViewSet
]
