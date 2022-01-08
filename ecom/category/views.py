from rest_framework import viewsets

from .serializers import ProductCategorySerializer
from .models import ProductCategory


class ProductCategoryViewset(viewsets.ModelViewSet):
    """ProductCategory viewset"""
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
