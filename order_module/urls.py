from django.urls import path
from .views import *

urlpatterns = [
    path('add-to-order', add_product_to_order, name='add-product-to-order')
]
