from django.urls import path

from charisma_product_module.views import CharismaProduct,ProductDetailView

urlpatterns = [
    path('', CharismaProduct.as_view(), name='charisma-products-list'),
    path('<slug:slug>', ProductDetailView.as_view(), name='charisma-product-detail'),

]
