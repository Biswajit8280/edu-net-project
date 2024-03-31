

# Create your views here.
# notes/views.py

from django.shortcuts import render

def registration(request):
    return render(request, 'registration.html')

def student_login(request):
    return render(request, 'student_login.html')

def teacher_login(request):
    return render(request, 'teacher_login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
