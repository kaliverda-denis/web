from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(help_text="Сіль, цукор, борошно")

    def __str__(self):
        return self.name
