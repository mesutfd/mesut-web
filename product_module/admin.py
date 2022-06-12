import decimal

from autoslug.settings import slugify
from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_editable = ['price']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['delete', 'apply_discount']

    @admin.action(description='افزودن موارد به لیست حذف شده ها (آیتم در دیتابیس باقی خواهد ماند.)')
    def delete(self, request, queryset):
        queryset.update(is_delete=True)

    @admin.action(description='اعمال 10 درصد تخفیف')
    def apply_discount(self, request, queryset):
        for product in queryset:
            product.price = product.price * decimal.Decimal('0.9')
            product.save()


class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'ip']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductVisit, ProductVisitAdmin)
admin.site.register(models.ProductGallery)
