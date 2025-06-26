# products/context_processors.py

from .models import Category

def compare_context(request):
    compare_list = request.session.get('compare_list', [])
    categories = Category.objects.all()  # Lấy tất cả danh mục
    
    return {
        'compare_list': compare_list,
        'categories': categories,  # Trả về danh sách danh mục
    }