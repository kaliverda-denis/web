from rest_framework import viewsets
from .models import Author, Book, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ВИПРАВЛЕНО: Видалено зайву функцію create_book(), тому що BookViewSet
# (ModelViewSet) вже має вбудований POST/create ендпоінт.
# Окремий create_book був дублікатом і до того ж повертав status=200 замість 201.


# ДОДАНО: ViewSet для відгуків (reviews)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
