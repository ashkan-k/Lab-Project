from django.contrib import admin
from .models import MedicalTest, Reception
from django.utils.html import format_html


# Register your models here.

@admin.register(MedicalTest)
class MedicalTestAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'price', 'created_at']
    search_fields = ('name', 'code', 'price')


@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ['medical_tests', 'full_name', 'age', 'mobile_phone', 'national_id', 'doctors', 'created_at']
    search_fields = ('full_name', 'medical_tests', 'national_id')
