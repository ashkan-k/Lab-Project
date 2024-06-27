from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from receptions.api.serializers import ReceptionSerializer
from receptions.models import Reception
from rest_framework import filters


class ReceptionVS(ListModelMixin, GenericViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'age', 'mobile_phone', 'home_phone', 'national_id', 'insurance__name',
                     'doctors__full_name']
