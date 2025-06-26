# products/urls.py

from django.urls import path
from . import views

# Dòng app_name = 'products' đã được xóa bỏ để loại bỏ namespace

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('compare/toggle/<int:pk>/', views.toggle_compare, name='toggle_compare'),
    path('compare/', views.compare_products, name='compare_products'),
]