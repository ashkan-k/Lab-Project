from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from acl.mixins import SuperUserRequiredMixin, VerifiedUserMixin, PermissionMixin
from .filters import ReceptionFilters, MedicalTestFilters
from .models import MedicalTest, Reception
from .forms import ReceptionForm, MedicalTestForm


# Create your views here.

# ===================================== Medical Test =====================================
class MedicalTestListView(PermissionMixin, ListView):
    permissions = ['tests_list']
    model = MedicalTest
    context_object_name = 'medicals'
    ordering = ['-updated_at']
    template_name = 'reception/medical/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return MedicalTestFilters(data=self.request.GET, queryset=queryset).qs


class MedicalTestCreateView(PermissionMixin, CreateView):
    permissions = ['tests_create']
    template_name = "reception/medical/form.html"
    model = MedicalTest
    form_class = MedicalTestForm
    success_url = reverse_lazy("medical-list")


class MedicalTestUpdateView(PermissionMixin, UpdateView):
    permissions = ['tests_edit']
    template_name = "reception/medical/form.html"
    model = MedicalTest
    form_class = MedicalTestForm
    success_url = reverse_lazy("medical-list")


class MedicalTestDeleteView(PermissionMixin, DeleteView):
    permissions = ['tests_delete']
    model = MedicalTest
    template_name = 'reception/medical/confirm_delete.html'
    success_url = reverse_lazy("medical-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response


# ===================================== Reception =====================================

class ReceptionListView(PermissionMixin, ListView):
    permissions = ['receptions_list']
    model = Reception
    context_object_name = 'receptions'
    ordering = ['-created_at']
    template_name = 'reception/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ReceptionFilters(data=self.request.GET, queryset=queryset).qs


class ReceptionCreateView(PermissionMixin, CreateView):
    permissions = ['receptions_create']
    template_name = "reception/form.html"
    model = Reception
    form_class = ReceptionForm
    success_url = reverse_lazy("reception-list")


class ReceptionUpdateView(PermissionMixin, UpdateView):
    permissions = ['receptions_edit']
    template_name = "reception/form.html"
    model = Reception
    form_class = ReceptionForm
    success_url = reverse_lazy("reception-list")


class ReceptionDeleteView(PermissionMixin, DeleteView):
    permissions = ['receptions_delete']
    model = Reception
    template_name = 'reception/confirm_delete.html'
    success_url = reverse_lazy("reception-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response
