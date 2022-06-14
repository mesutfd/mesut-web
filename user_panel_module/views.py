from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from order_module.models import Order, OrderDetail
from .forms import *
from account_module.models import User
from .forms import EditProfileModelForm


@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form': edit_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


@login_required(login_url='login_page')
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')


@method_decorator(login_required, name='dispatch')
class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        current_user: User = User.objects.filter(id=request.user.id).first()
        context = {
            'form': ChangePasswordForm(),
            'current_user': current_user

        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data['current_password']):
                current_user.set_password(form.cleaned_data['new_password'])
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('current_password', 'کلمه عبور فعلی وارد شده صحیح نمیباشد.')
        context = {
            'form': form,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/change_password_page.html', context)


@login_required(login_url='login_page')
def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel_module/user_basket.html', context)


@login_required(login_url='login_page')
def remove_order_detail(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    deleted_count, deleted_dict = OrderDetail.objects.filter(
        id=detail_id,
        order__is_paid=False,
        order__user_id=request.user.id,
    ).delete()

    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found',
        })

    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)

    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })


@login_required(login_url='login_page')
def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })
    order_detail = OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                              order__user_id=request.user.id).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found',
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid',
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel_module/user_basket_content.html', context)
