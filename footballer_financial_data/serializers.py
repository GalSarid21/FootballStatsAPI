from rest_framework import serializers
from .models import FootballerFinancialData

class FootballerFinancialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballerFinancialData
        fields = '__all__' 

class FootballerFinancialDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballerFinancialData
        fields = ['net_worth','currency','other_professions','last_update']