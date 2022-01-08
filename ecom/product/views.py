from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Product


class ProductViewset(viewsets.ModelViewSet):
    """Product viewset"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
