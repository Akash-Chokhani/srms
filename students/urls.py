from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('students/<roll>', views.results, name='result'),
    path('branch/', views.branch, name='branch'),
    path('branch/<bcode>', views.branch_subjects, name='branch_sub'),
    path('subjects/', views.subjects, name='subjects'),
    path('marks/', views.marks, name='marks'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<roll>', views.delete, name='delete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('delete/<roll>', views.delete, name="delete"),
    path('search', views.search, name="search"),
    path('edit/<roll>', views.edit, name="edit")
]
