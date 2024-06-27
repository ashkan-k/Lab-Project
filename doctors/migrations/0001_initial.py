# Generated by Django 5.0.6 on 2024-06-17 23:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='نام پزشک')),
                ('specialization', models.CharField(max_length=255, verbose_name='تخصص')),
                ('contact_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='شماره موبایل معتبر نیست.', regex='(^\\+?(09|98|0)?(9([0-9]{9}))$)')], verbose_name='شماره تماس')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='تصویر')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
            ],
            options={
                'verbose_name': 'پزشک',
                'verbose_name_plural': 'پزشکان',
            },
        ),
    ]