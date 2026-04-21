"""
Root URL configuration.

This file is CORRECT — do not change it while debugging.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('catalog.urls')),
    path('api/', include('loans.urls')),
]
