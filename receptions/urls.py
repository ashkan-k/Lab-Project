from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('medical/test/', MedicalTestListView.as_view(), name='medical-list'),
    path('medical/test/create/', MedicalTestCreateView.as_view(), name='medical-create'),
    path('medical/test/update/<int:pk>/', MedicalTestUpdateView.as_view(), name='medical-update'),
    path('medical/test/delete/<int:pk>/', MedicalTestDeleteView.as_view(), name='medical-delete'),

    path('', ReceptionListView.as_view(), name='reception-list'),
    path('create/', ReceptionCreateView.as_view(), name='reception-create'),
    path('update/<int:pk>/', ReceptionUpdateView.as_view(), name='reception-update'),
    path('delete/<int:pk>/', ReceptionDeleteView.as_view(), name='reception-delete'),
]

urlpatterns += dashboard_urls
