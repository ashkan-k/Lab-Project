from django.db import models
from datetime import time
from django.utils.text import slugify
from extenstions.utils import jalali_converter

# Create your models here.


def upload_image(instance, filename):
    path = 'uploads/' + 'items/' + \
           slugify(instance.full_name, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.full_name) + '-' + filename
    return path + '/' + name


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    quantity = models.IntegerField(verbose_name="تعداد")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت")
    image = models.ImageField(
        ('تصویر'), upload_to='uploads/', null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name="وضعیت")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'انبار'
        verbose_name_plural = 'انبارداری'

    def jcreated(self):
        return jalali_converter(self.created_at)

    @property
    def get_status(self):
        return 'تایید شده' if self.status else 'تایید نشده'
