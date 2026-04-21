# ВИПРАВЛЕНО: Замінено 'from django.contrib.auth.models import User' на settings.AUTH_USER_MODEL,
# тому що проєкт використовує CustomUser (AUTH_USER_MODEL = 'users.CustomUser')
from django.conf import settings
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()
    available_copies = models.IntegerField(default=1)

    # ДОДАНО: Метод для обчислення середнього рейтингу (avg_rating)
    @property
    def avg_rating(self):
        reviews = self.reviews.all()
        if not reviews.exists():
            return None
        return round(reviews.aggregate(models.Avg('mark'))['mark__avg'], 2)

    def __str__(self):
        return self.title


# ДОДАНО: Модель Review з полями mark та text (reviews ← mark, text)
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    mark = models.PositiveSmallIntegerField()  # оцінка (1-5)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'user')  # один відгук від користувача на книгу

    def __str__(self):
        return f"Review by {self.user} on {self.book} — {self.mark}/5"
