# ВИПРАВЛЕНО: Замінено 'from django.contrib.auth.models import User' на settings.AUTH_USER_MODEL,
# тому що проєкт використовує CustomUser (AUTH_USER_MODEL = 'users.CustomUser')
from django.conf import settings
from django.db import models
from catalog.models import Book


class Loan(models.Model):
    # ВИПРАВЛЕНО: Замінено User на settings.AUTH_USER_MODEL
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
