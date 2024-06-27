from rest_framework import serializers
from receptions.models import Reception


class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'
