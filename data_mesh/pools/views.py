import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (MOCK_POOLS_DATA)


@api_view(['GET', 'POST'])
def pool_list(request, format=None):
    # Retrieve all pools
    if request.method == 'GET':
        return Response(MOCK_POOLS_DATA, status=status.HTTP_200_OK)

    # Create a pool
    if request.method == 'POST':
        return Response(MOCK_POOLS_DATA[0], status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def pool_detail(request, name, format=None):

    # Retrieve a pool
    if request.method == 'GET':
        return Response(MOCK_POOLS_DATA[0], status=status.HTTP_200_OK)

    # Update a pool
    elif request.method == 'PUT':
        return Response(MOCK_POOLS_DATA[0], status=status.HTTP_200_OK)

    # Delete a pool
    elif request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
