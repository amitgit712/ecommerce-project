from django.db import models

from category.models import ProductCategory


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.FileField(
            upload_to='images/product/',
            null=True, blank=True
            )
    sku = models.CharField(max_length=250)
    category = models.ForeignKey(
            ProductCategory, on_delete=models.CASCADE,
            null=True, blank=True
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
