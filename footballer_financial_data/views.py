from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FootballerFinancialData
from .serializers import FootballerFinancialDataSerializer, FootballerFinancialDataUpdateSerializer
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
def get_by_net_worth(request, net_worth):
    try:
        include_greaters_str = request.query_params.get('include-greaters')
        include_greaters = (False if include_greaters_str is None 
                                  else include_greaters_str.lower() == 'true')
        footballers = DbAccessFunctions.get_footballers_by_net_worth(net_worth, include_greaters)
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
    serializer = FootballerFinancialDataSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)
    try:
        footballers = DbAccessFunctions.add_footballers(serializer.validated_data)
        serializer = FootballerFinancialDataSerializer(footballers, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update(request, id):
    is_input_partial = 'full_name' not in request.data and 'nationality' not in request.data
    if is_input_partial:
        serializer = FootballerFinancialDataUpdateSerializer(data=request.data, many=False)
    else:
        serializer = FootballerFinancialDataSerializer(data=request.data, many=False)
    serializer.is_valid(raise_exception=True)
    try:
        footballer = DbAccessFunctions.update_footballer(serializer.validated_data, id, is_input_partial)
        serializer = FootballerFinancialDataSerializer(footballer)
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','DELETE'])
def delete(request, id):
    try:
        DbAccessFunctions.delete_footballer(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
