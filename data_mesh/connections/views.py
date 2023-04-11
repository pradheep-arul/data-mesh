import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (MOCK_CONNECTIONS_DATA)


@api_view(['GET', 'POST'])
def connection_list(request, format=None):
    # Retrieve all connections
    if request.method == 'GET':
        return Response(MOCK_CONNECTIONS_DATA, status=status.HTTP_200_OK)

    # Create a connection
    if request.method == 'POST':
        return Response(MOCK_CONNECTIONS_DATA[0], status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def connection_detail(request, name, format=None):

    # Retrieve a connection
    if request.method == 'GET':
        return Response(MOCK_CONNECTIONS_DATA[0], status=status.HTTP_200_OK)

    # Update a connection
    elif request.method == 'PUT':
        return Response(MOCK_CONNECTIONS_DATA[0], status=status.HTTP_200_OK)

    # Delete a connection
    elif request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
