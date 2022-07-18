from django.db import models

import product_module.models


class PaymentStatus(models.Model):
    payment_id = models.TextField(max_length=255, verbose_name='مشخصات خرید')
    product = models.ForeignKey(product_module.models.Product, null=True, blank=True, on_delete=models.CASCADE,
                                verbose_name='کالا')
