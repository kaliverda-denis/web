from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_recipe),
    path('edit/<int:pk>/', views.edit_recipe),
    path('delete/<int:pk>/', views.delete_recipe),
]