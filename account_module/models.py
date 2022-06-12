from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile/', null=True, blank=True, verbose_name='آواتار')
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه')
    email_active_code = models.CharField(max_length=100,editable=False, verbose_name='کد فعالسازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره کاربر')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is "" and self.last_name == "":
            return self.username
        return self.get_full_name()
