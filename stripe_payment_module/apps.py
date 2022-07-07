from django.apps import AppConfig


class StripePaymentModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stripe_payment_module'
    verbose_name = 'درگاه استرایپ'
