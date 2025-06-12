# products/admin.py
from django.contrib import admin
from .models import Category, Camera

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'original_price', 'is_bestseller')
    list_filter = ('category', 'is_bestseller')
    search_fields = ('name', 'description')

    # Sắp xếp lại các trường trong form edit cho gọn gàng
    fieldsets = (
        ('Thông tin chung', {
            'fields': ('category', 'name', 'image', 'description')
        }),
        ('Giá & Khuyến mãi', {
            'fields': ('price', 'original_price', 'is_bestseller')
        }),
        ('Thông số kỹ thuật ngắn', {
            'fields': ('spec_line_1', 'spec_line_2', 'spec_line_3')
        }),
        ('Thông số kỹ thuật khác', {
            'fields': ('resolution',)
        }),
    )