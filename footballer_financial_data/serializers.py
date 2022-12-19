from rest_framework import serializers
from .models import FootballerFinancialData

class FootballerFinancialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballerFinancialData
        fields = '__all__' 