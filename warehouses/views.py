from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from acl.mixins import PermissionMixin
from .filters import ItemFilters
from .models import Item
from .forms import ItemForm


# Create your views here.
class ItemListView(PermissionMixin, ListView):
    permissions = ['warehouses_list']
    model = Item
    context_object_name = 'items'
    ordering = ['-created_at']
    template_name = 'warehouses/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ItemFilters(data=self.request.GET, queryset=queryset).qs


class ItemCreateView(PermissionMixin, CreateView):
    permissions = ['warehouses_create']
    template_name = "warehouses/form.html"
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("warehouses-list")


class ItemUpdateView(PermissionMixin, UpdateView):
    permissions = ['warehouses_edit']
    template_name = "warehouses/form.html"
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy("warehouses-list")


class ItemDeleteView(PermissionMixin, DeleteView):
    permissions = ['warehouses_delete']
    model = Item
    template_name = 'warehouses/confirm_delete.html'
    success_url = reverse_lazy("warehouses-list")

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حذف شد.')
        return response
