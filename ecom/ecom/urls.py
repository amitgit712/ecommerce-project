from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('account.urls')),
    # path('', include('category.urls')),
    # path('', include('order.urls')),
    # path('', include('payment.urls')),
    path('', include('product.urls')),
]
