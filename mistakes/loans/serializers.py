from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

    def create(self, validated_data):
        book = validated_data['book']

        # ВИПРАВЛЕНО: Додано валідацію available_copies перед створенням позики.
        # Перевіряємо що є доступні копії книги (available_copies > 0)
        if book.available_copies <= 0:
            raise serializers.ValidationError(
                "No available copies of this book."
            )

        loan = Loan.objects.create(**validated_data)
        book.available_copies -= 1
        book.save()
        return loan
