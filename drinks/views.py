# create endpoint(URL) to access the data at here
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    # GET method is used to get data
    if request.method == 'GET':
        # for GET request(ask for data)
        # get all the drinks
        drinks = Drink.objects.all()
        # serialize the data
        serializer = DrinkSerializer(drinks, many=True)
        # return the serialized data(JSON)
        # in order to allow non-dict objects to be serialized set the safe parameter to False
        # since we are in dict, so can set safe to True
        # change the return result to Response serializer.data
        return Response(serializer.data)

    # POST method is used to post data
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# attribute for the drink_detail function, get, put, delete


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    # pk is primary key
    # get the drink by id
    # it is to make sure the drink exists
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # get the data of the drink
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # update the data of the drink
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
