from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from receptions.models import Reception, MedicalTest
from users.models import User


# Create your views here.


class DashboardView(View):
    template_name = "./admin/home.html"

    def get(self, request, *args, **kwargs):
        receptions = Reception.objects.order_by('-created_at')[:3]
        context = {
            'receptions': receptions,
            'receptions_count': Reception.objects.count(),
            'medical_test_count': MedicalTest.objects.count(),
            'user_count': User.objects.count(),
        }
        return render(request, self.template_name, context)
