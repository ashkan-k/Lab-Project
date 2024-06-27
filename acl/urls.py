from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('roles/', RolesListView.as_view(), name='roles-list'),
    path('roles/create/', RolesCreateView.as_view(), name='roles-create'),
    path('roles/update/<int:pk>/', RolesUpdateView.as_view(), name='roles-update'),
    path('roles/delete/<int:pk>/', RolesDeleteView.as_view(), name='roles-delete'),

    path('permissions/', PermissionsListView.as_view(), name='permissions-list'),
    path('permissions/create/', PermissionsCreateView.as_view(), name='permissions-create'),
    path('permissions/update/<int:pk>/', PermissionsUpdateView.as_view(), name='permissions-update'),
    path('permissions/delete/<int:pk>/', PermissionsDeleteView.as_view(), name='permissions-delete'),

    path('role/user/', RoleUserListView.as_view(), name='role-user-list'),
    path('role/user/create/', RoleUserCreateView.as_view(), name='role-user-create'),
    path('role/user/update/<int:pk>/', RoleUserUpdateView.as_view(), name='role-user-update'),
    path('role/user/delete/<int:pk>/', RoleUserDeleteView.as_view(), name='role-user-delete'),
]

urlpatterns += dashboard_urls
