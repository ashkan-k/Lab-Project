from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from acl.mixins import SuperUserRequiredMixin, VerifiedUserMixin, PermissionMixin
from .filters import DoctorFilters
from .models import Doctor
from .forms import DoctorForm


# Create your views here.

class DoctorsListView(PermissionMixin, ListView):
    permissions = ['doctors_list']
    model = Doctor
    context_object_name = 'doctors'
    ordering = ['-updated_at']
    template_name = 'doctors/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return DoctorFilters(data=self.request.GET, queryset=queryset).qs


class DoctorsCreateView(PermissionMixin, CreateView):
    permissions = ['doctors_create']
    template_name = "doctors/form.html"
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("doctor-list")


class DoctorsUpdateView(PermissionMixin, UpdateView):
    permissions = ['doctors_edit']
    template_name = "doctors/form.html"
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("doctor-list")


class DoctorDeleteView(PermissionMixin, DeleteView):
    permissions = ['doctors_delete']
    model = Doctor
    template_name = 'doctors/confirm_delete.html'
    success_url = reverse_lazy("doctor-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response
