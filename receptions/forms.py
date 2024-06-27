from django import forms
from .models import Reception, MedicalTest


class MedicalTestForm(forms.ModelForm):
    class Meta:
        model = MedicalTest
        fields = "__all__"


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = "__all__"
