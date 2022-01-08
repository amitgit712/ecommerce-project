from rest_framework import serializers

from .models import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    """Productcategory seriaalizer"""
    image = serializers.FileField(
            max_length=None, allow_empty_file=False,
            allow_null=True, required=False
            )

    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description', 'image')
        read_only_fields = ('id',)
