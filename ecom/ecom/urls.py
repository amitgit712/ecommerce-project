from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('account.urls')),
    path('category/', include('category.urls')),
    # path('', include('order.urls')),
    # path('', include('payment.urls')),
    path('product/', include('product.urls')),
]
