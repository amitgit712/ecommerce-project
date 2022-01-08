from django.urls import path, include

from rest_framework.routers import DefaultRouter

from category import views


router = DefaultRouter()
router.register('product-categorys', views.ProductCategoryViewset)

app_name = 'category'

urlpatterns = [
    path('', include(router.urls)),
]
