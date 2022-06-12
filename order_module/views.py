from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from order_module.models import Order, OrderDetail
from product_module.models import Product


# Create your views here.


def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مثدار وارد شده معتبر نیست',
            'confirm_button_text': 'حله دا',
            'confirm_message': 'تصحیح شد',
            'icon': 'error',
        })

    if request.user.is_authenticated:

        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success ',
                'text': 'با موفقیت اضافه شد',
                'confirm_button_text': 'دمت گرم',
                'confirm_message': 'انجام شد ;)',
                'icon': 'success',
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'confirm_button_text': 'باع!',
                'confirm_message': 'تصحیح شد',

                'icon': 'question',
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای خرید باید ابتدا وارد شوید',
            'confirm_button_text': 'ورود به سایت',
            'confirm_message': 'ورود به سایت',

            'icon': 'warning',
        })
