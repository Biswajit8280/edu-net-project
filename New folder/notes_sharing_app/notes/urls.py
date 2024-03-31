# notes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('student_login/', views.student_login, name='student_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
