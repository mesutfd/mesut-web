from django.urls import path

from stripe_payment_module.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
    SuccessView,
    CancelView,
    stripe_webhook,
    StripeIntentView
)

urlpatterns = [
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('check_payment/', SuccessView.as_view(), name='success'),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
