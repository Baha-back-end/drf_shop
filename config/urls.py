from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # API urls
    path('api/common/', include('common.urls')),
    path('api/services/', include('services.urls')),
    path('api/products/',include('products.urls')),
    path('api/clinics/', include('clinics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)