# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Camera, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request):
    category_slug = request.GET.get('category')
    query = request.GET.get('q')
    compare_list = request.session.get('compare_list', [])

    categories = Category.objects.all()
    cameras = Camera.objects.all()

    if category_slug:
        cameras = cameras.filter(category__slug=category_slug)
    if query:
        cameras = cameras.filter(name__icontains=query)

    paginator = Paginator(cameras, 6)
    page_number = request.GET.get('page')
    try:
        paginated_cameras = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_cameras = paginator.page(1)
    except EmptyPage:
        paginated_cameras = paginator.page(paginator.num_pages)

    context = {
        'cameras': paginated_cameras,
        'categories': categories,
        'compare_list': compare_list,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    camera = get_object_or_404(Camera, pk=pk)
    context = {
        'camera': camera
    }
    return render(request, 'products/product_detail.html', context)

def toggle_compare(request, pk):
    compare_list = request.session.get('compare_list', [])
    if pk in compare_list:
        compare_list.remove(pk)
    else:
        if len(compare_list) < 3:
            compare_list.append(pk)
    request.session['compare_list'] = compare_list
    return redirect('product_list')

# VIEW MỚI CHO TRANG SO SÁNH
def compare_products(request):
    compare_list_ids = request.session.get('compare_list', [])
    # Lấy các đối tượng camera có pk nằm trong list id đã lưu
    cameras = Camera.objects.filter(pk__in=compare_list_ids)
    context = {
        'cameras': cameras
    }
    return render(request, 'products/compare_products.html', context)