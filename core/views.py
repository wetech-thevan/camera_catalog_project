# core/views.py

from django.shortcuts import render
from products.models import Category, Camera

def home(request):
    # Lấy 5 sản phẩm được đánh dấu là "bán chạy"
    bestsellers = Camera.objects.filter(is_bestseller=True)[:5]
    
    # Lấy danh mục "Camera Giám Sát" và 5 sản phẩm của nó
    try:
        surveillance_category = Category.objects.get(name__iexact="Camera Giám Sát")
        surveillance_cameras = Camera.objects.filter(category=surveillance_category)[:5]
    except Category.DoesNotExist:
        surveillance_category = None
        surveillance_cameras = []

    # --- PHẦN BỊ THIẾU TRƯỚC ĐÂY ĐÃ ĐƯỢC BỔ SUNG LẠI ---
    context = {
        'bestsellers': bestsellers,
        'surveillance_category': surveillance_category,
        'surveillance_cameras': surveillance_cameras,
    }
    # --- KẾT THÚC PHẦN BỔ SUNG ---

    # Phần code lấy các danh mục sản phẩm khác cho các khối 5 sản phẩm
    # Bạn có thể giữ lại hoặc tạm thời bỏ đi nếu muốn trang chủ gọn hơn
    def get_products_by_category_slug(slug):
        try:
            category = Category.objects.get(slug=slug)
            products = category.cameras.all()[:5]
            return category, products
        except Category.DoesNotExist:
            return None, []

    indoor_cat, indoor_products = get_products_by_category_slug('camera-trong-nha')
    outdoor_cat, outdoor_products = get_products_by_category_slug('camera-ngoai-troi')
    kit_cat, kit_products = get_products_by_category_slug('bo-kit-imou')
    accessory_cat, accessory_products = get_products_by_category_slug('phu-kien')
    
    # Cập nhật context với đầy đủ các biến
    context.update({
        'hot_sale_products': bestsellers, # Tạm dùng bestsellers cho hot sale
        'indoor_cat': indoor_cat,
        'indoor_products': indoor_products,
        'outdoor_cat': outdoor_cat,
        'outdoor_products': outdoor_products,
        'kit_cat': kit_cat,
        'kit_products': kit_products,
        'accessory_cat': accessory_cat,
        'accessory_products': accessory_products,
    })

    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def login_view(request):
    from django.shortcuts import redirect
    return redirect('home')