from django.contrib import admin

from .models import User, ShippingAddress

admin.site.register(User)
admin.site.register(ShippingAddress)
