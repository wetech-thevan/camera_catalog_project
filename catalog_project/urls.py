# catalog_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Thêm dòng này
from django.conf.urls.static import static # Thêm dòng này

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls')), # Sẽ thêm ở bước sau
]

# Cấu hình để phục vụ file media trong môi trường development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)