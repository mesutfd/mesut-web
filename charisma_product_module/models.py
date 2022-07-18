from django.db import models

# Create your models here.

from account_module.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    url_title = models.CharField(max_length=700, verbose_name='نام برند در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    class BreakableChoices(models.TextChoices):
        beakable = ('breakable', 'شکستنی')
        un_beakable = ('un_beakable', 'غیر شکستنی')

    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    is_breakable = models.CharField(max_length=255, choices=BreakableChoices.choices, verbose_name='آیا شکستنیست؟')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(null=False, db_index=True, max_length=400, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    tax = models.IntegerField(editable=False , null=True, blank=True, verbose_name='مالیات')

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    #
    # def get_absolute_url(self):
    #     return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        if not self.tax:
            self.tax = self.price * 0.09
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    def get_absolute_url(self):
        return reverse('charisma-product-detail', args=[self.slug])

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
