from django.shortcuts import render
from .models import Department, Instructor

def department_list(request):
    departments = Department.objects.all()
    instructors = Instructor.objects.all()
    
    return render(request, 'departments/list.html', {
        'departments': departments,
        'instructors': instructors
    })