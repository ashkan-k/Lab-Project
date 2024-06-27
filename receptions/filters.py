import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class MedicalTestFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    type = filters.CharFilter(method="type_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(name__icontains=value) |
            Q(code__icontains=value) |
            Q(price__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs


class ReceptionFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    type = filters.CharFilter(method="type_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            # Q(medicaltest__name__icontains=value) |
            Q(full_name__icontains=value) |
            Q(age__icontains=value) |
            Q(mobile_phone__icontains=value) |
            Q(home_phone__icontains=value) |
            Q(national_id__icontains=value) |
            Q(insurance__name__icontains=value) |
            Q(doctors__full_name__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs
