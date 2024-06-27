from django.db import models
from utils.validator import mobile_regex, mobile_validator, national_id_regex
from doctors.models import Doctor
from extenstions.utils import jalali_converter
from insurances.models import Insurance

# Create your models here.

SUPPLEMENTARY_INSURANCE_STATUS_CHOICES = (
    ('YES', 'دارد'),
    ('NO', 'ندارد'),
)

MEDICAL_TEST_STATUS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)


class MedicalTest(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام ازمایش')
    code = models.CharField(
        max_length=128,
        verbose_name='کد ازمایش',
        choices=MEDICAL_TEST_STATUS_CHOICES,
    )
    price = models.FloatField(verbose_name="قیمت")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )

    def __str__(self):
        return f"{self.name} | {self.code} "

    class Meta:
        verbose_name = 'ازمایش'
        verbose_name_plural = 'ازمایش ها'

    def jcreated(self):
        return jalali_converter(self.created_at)


class Reception(models.Model):
    medical_tests = models.ForeignKey(MedicalTest, on_delete=models.CASCADE, verbose_name="ازمایش")
    full_name = models.CharField(max_length=150, verbose_name="نام بیمار")
    age = models.IntegerField(verbose_name="سن")
    mobile_phone = models.CharField(max_length=11, verbose_name="همراه")
    home_phone = models.CharField(max_length=11, verbose_name="تلفن")
    national_id = models.CharField(
        unique=True,
        max_length=10,
        default="",
        verbose_name="کد ملی",
        validators=[national_id_regex],
    )
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, verbose_name="بیمه")
    supplementary_insurance = models.CharField(
        max_length=128,
        verbose_name='تکمیلی',
        choices=SUPPLEMENTARY_INSURANCE_STATUS_CHOICES,
    )
    version_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ نسخه"
    )
    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="receptions_doctors",
                                verbose_name="پزشک")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )

    def __str__(self):
        return f"{self.full_name} | {self.national_id} | {self.medical_tests}"

    class Meta:
        verbose_name = 'پذیرش'
        verbose_name_plural = 'پذیرش ها'

    def jcreated(self):
        return jalali_converter(self.created_at)
