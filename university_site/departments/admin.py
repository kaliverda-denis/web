from .models import Department, Instructor
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Instructor)