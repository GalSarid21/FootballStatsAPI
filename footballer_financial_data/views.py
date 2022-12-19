from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FootballerFinancialData
from .serializers import FootballerFinancialDataSerializer
from .repository import DbAccessFunctions 

@api_view(['GET'])
def ping(request):
    return Response('pong')

@api_view(['GET'])
def get_all(request):
    try:
        footballers = DbAccessFunctions.get_all_footballers()
        serializer = FootballerFinancialDataSerializer(footballers, many=True)
        return Response(serializer.data)
    except FootballerFinancialData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_by_full_name(request, full_name):
    try:
        footballer = DbAccessFunctions.get_footballer_by_full_name(full_name)
        serializer = FootballerFinancialDataSerializer(footballer)
        return Response(serializer.data)
    except FootballerFinancialData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get(request, id):
    try:
        footballer = DbAccessFunctions.get_footballer_by_id(id)
        serializer = FootballerFinancialDataSerializer(footballer)
        return Response(serializer.data)
    except FootballerFinancialData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add(request):
    serializer = FootballerFinancialDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        DbAccessFunctions.add_footballer(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

