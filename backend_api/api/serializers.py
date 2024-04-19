from backend_api.models import *
from rest_framework import serializers


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralReport
        fields = '__all__'
