# core/views.py
from django.shortcuts import render
from products.models import Camera, Category

def home(request):
    bestsellers = Camera.objects.filter(is_bestseller=True)[:4]

    # Khởi tạo các biến để tránh lỗi nếu không tìm thấy
    surveillance_category = None
    surveillance_cameras = []
    outdoor_category = None
    outdoor_cameras = []

    try:
        surveillance_category = Category.objects.get(name__iexact="Camera Giám Sát")
        surveillance_cameras = Camera.objects.filter(category=surveillance_category)[:4]
    except Category.DoesNotExist:
        pass # Bỏ qua nếu không tìm thấy danh mục

    try:
        outdoor_category = Category.objects.get(name__iexact="Camera Ngoài Trời")
        outdoor_cameras = Camera.objects.filter(category=outdoor_category)[:4]
    except Category.DoesNotExist:
        pass # Bỏ qua nếu không tìm thấy danh mục

    context = {
        'bestsellers': bestsellers,
        'surveillance_category': surveillance_category, # Gửi đối tượng danh mục
        'surveillance_cameras': surveillance_cameras,
        'outdoor_category': outdoor_category,       # Gửi đối tượng danh mục
        'outdoor_cameras': outdoor_cameras,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')