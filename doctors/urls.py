from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('', DoctorsListView.as_view(), name='doctor-list'),
    path('create/', DoctorsCreateView.as_view(), name='doctor-create'),
    path('update/<int:pk>/', DoctorsUpdateView.as_view(), name='doctor-update'),
    path('delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor-delete'),
]

urlpatterns += dashboard_urls
