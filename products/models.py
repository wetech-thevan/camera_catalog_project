# products/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tên danh mục")
    slug = models.SlugField(max_length=255, unique=True, help_text="Phần thân thiện với URL, tự động tạo từ tên nếu để trống.")

    class Meta:
        verbose_name = "Danh mục"
        verbose_name_plural = "Các danh mục"

    def __str__(self):
        return self.name

class Camera(models.Model):
    category = models.ForeignKey(Category, related_name='cameras', on_delete=models.SET_NULL, null=True, verbose_name="Danh mục")
    name = models.CharField(max_length=255, verbose_name="Tên sản phẩm")
    description = models.TextField(verbose_name="Mô tả sản phẩm")

    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Giá bán")
    # --- CÁC TRƯỜNG MỚI ---
    original_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, verbose_name="Giá gốc (nếu có)")

    spec_line_1 = models.CharField(max_length=255, blank=True, verbose_name="Dòng thông số 1")
    spec_line_2 = models.CharField(max_length=255, blank=True, verbose_name="Dòng thông số 2")
    spec_line_3 = models.CharField(max_length=255, blank=True, verbose_name="Dòng thông số 3")
    # --- KẾT THÚC CÁC TRƯỜNG MỚI ---

    image = models.ImageField(upload_to='cameras/', verbose_name="Hình ảnh sản phẩm")
    resolution = models.CharField(max_length=100, blank=True, verbose_name="Độ phân giải")
    is_bestseller = models.BooleanField(default=False, verbose_name="Là sản phẩm bán chạy?")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        verbose_name = "Camera"
        verbose_name_plural = "Các Camera"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    # --- THUỘC TÍNH MỚI ĐỂ TÍNH GIẢM GIÁ ---
    @property
    def discount_percent(self):
        if self.original_price and self.original_price > self.price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return int(round(discount, 0))
        return 0