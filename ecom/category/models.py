from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=200)
    image = models.FileField(
            upload_to='images/product/',
            blank=True, null=True
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
