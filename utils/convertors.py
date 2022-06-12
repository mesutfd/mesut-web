import decimal


def group_list_convertor(custom_list, size=4):
    grouped_list = []
    for i in range(0, len(custom_list), size):
        grouped_list.append(custom_list[i:i + size])
    return grouped_list


def apply_discount(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * decimal.Decimal('0.9')
        product.save()


apply_discount.short_description = 'اعمال 10 درصد تخفیف'
