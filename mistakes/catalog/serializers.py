from rest_framework import serializers
from .models import Author, Book, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # ДОДАНО: avg_rating — середній рейтинг книги з відгуків
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def validate_year(self, value):
        if value > 2026:
            raise serializers.ValidationError(
                "Year cannot be in the future"
            )
        return value


# ДОДАНО: Серіалізатор для моделі Review (mark, text)
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)

    def validate_mark(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Mark must be between 1 and 5."
            )
        return value
