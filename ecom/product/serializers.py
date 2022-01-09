from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product objects"""
    image = serializers.FileField(
            max_length=None, allow_empty_file=False,
            allow_null=True, required=False
            )

    class Meta:
        model = Product
        fields = (
                'id', 'name', 'description',
                'price', 'stock', 'sku',
                'image', 'category', 'created_at',
                'updated_at'
                )
        read_only_fields = ('id', 'created_at', 'updated_at',)
