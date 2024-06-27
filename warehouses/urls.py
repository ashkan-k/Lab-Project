from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('', ItemListView.as_view(), name='warehouses-list'),
    path('create/', ItemCreateView.as_view(), name='warehouses-create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='warehouses-update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='warehouses-delete'),
]

urlpatterns += dashboard_urls
