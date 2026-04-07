from django.urls import path
from . import views

urlpatterns = [

    path('', views.department_list, name='department-list'),


    path('api/departments/', views.department_api_list, name='department-api-list'),
    path('api/departments/<int:pk>/', views.department_api_detail, name='department-api-detail'),

 
    path('api/instructors/', views.instructor_api_list, name='instructor-api-list'),
    path('api/instructors/<int:pk>/', views.instructor_api_detail, name='instructor-api-detail'),

   
    path('api/login/', views.login_view, name='login'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/register/', views.register_view, name='register'),
]