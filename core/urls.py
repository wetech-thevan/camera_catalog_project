# core/urls.py

from django.urls import path
from . import views

# Dòng app_name = 'core' đã được xóa bỏ

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
]