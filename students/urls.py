from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('subjects/', views.subjects, name='subjects'),
    path('marks/', views.marks, name='marks'),
    path('test/', views.test, name='test'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
]
