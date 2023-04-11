from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('subjects/', views.subjects, name='subjects'),
    path('marks/', views.marks, name='marks'),
    path('test/', views.test, name='test'),
]
