from django.urls import path
from .views import products, details_Product

urlpatterns = [
    path('products/', products, name='products'), 
    path('products/<int:product_id>', details_Product, name='details_Product'), 
    
]