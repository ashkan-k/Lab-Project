from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Doctor


class DoctorAdmin(UserAdmin):
    ordering = ['contact_number']
    model = Doctor
    list_display = ['full_name', 'specialization', 'contact_number', 'image', 'created_at', 'updated_at']


admin.site.register(Doctor)
