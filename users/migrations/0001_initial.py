# Generated by Django 5.0.6 on 2024-06-13 22:46

import django.core.validators
import users.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='نام خانوادگی')),
                ('phoneNumber', models.CharField(max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='شماره موبایل معتبر نیست.', regex='(^\\+?(09|98|0)?(9([0-9]{9}))$)')], verbose_name='شماره موبایل')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('national_id', models.CharField(default='', max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='شناسه ملی معتبر نیست.', regex='^\\d{10}$')], verbose_name='کد ملی')),
                ('father_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='نام پدر')),
                ('marital_status', models.CharField(blank=True, choices=[('S', 'مجرد'), ('M', 'متاهل')], max_length=128, null=True, verbose_name='وضعیت تاهل')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
