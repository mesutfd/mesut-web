from django.urls import path
from .views import *

urlpatterns = [
    path('', UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('change-password', ChangePasswordPage.as_view(), name='change_password_page'),
    path('edit-profile', EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('user-basket', user_basket, name='user_basket_page'),
    path('remove-order-detail', remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', change_order_detail_count, name='change_order_detail_count_ajax'),
]
