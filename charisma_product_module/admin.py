from django.contrib import admin
from charisma_product_module.models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)