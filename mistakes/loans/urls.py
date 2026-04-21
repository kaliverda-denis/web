from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('loans', views.LoanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('loans-summary/', views.user_loans_summary, name='loans_summary'),
]
