from django.db import models

import product_module.models


class PaymentStatus(models.Model):
    payment_id = models.TextField(max_length=255, verbose_name='مشخصات خرید')
    models.ForeignKey(product_module.models.Product, on_delete=models.CASCADE, verbose_name='کالا')
