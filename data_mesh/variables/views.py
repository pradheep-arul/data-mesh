
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MOCK_VARIABLES_DATA


@api_view(['GET', 'POST'])
def variable_list(request, format=None):
    # Retrieve all variables
    if request.method == 'GET':
        return Response(MOCK_VARIABLES_DATA, status=status.HTTP_200_OK)

    # Create a variable
    if request.method == 'POST':
        return Response(MOCK_VARIABLES_DATA[0], status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def variable_detail(request, name, format=None):

    # Retrieve a variable
    if request.method == 'GET':
        return Response(MOCK_VARIABLES_DATA[0], status=status.HTTP_200_OK)

    # Update a variable
    elif request.method == 'PUT':
        return Response(MOCK_VARIABLES_DATA[0], status=status.HTTP_200_OK)

    # Delete a variable
    elif request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)
