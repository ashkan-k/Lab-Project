from datetime import time

from django.db import models
from utils.validator import mobile_regex
from django.utils.text import slugify
from extenstions.utils import jalali_converter


# Create your models here.

def upload_image(instance, filename):
    path = 'uploads/' + 'doctors/' + \
           slugify(instance.full_name, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.full_name) + '-' + filename
    return path + '/' + name


class Doctor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="نام پزشک")
    specialization = models.CharField(max_length=255, verbose_name="تخصص")
    contact_number = models.CharField(verbose_name="شماره تماس", max_length=20, unique=True, validators=[mobile_regex])
    image = models.ImageField(('تصویر'), upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'پزشک'
        verbose_name_plural = 'پزشکان'

    def jcreated(self):
        return jalali_converter(self.created_at)
