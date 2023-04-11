import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MOCK_TRANSFORMATION_DATA, Transformation
from .serializers import TransformationSerializer


@api_view(['GET', 'POST'])
def transformation_list(request, format=None):
    # Retrieve all transformations
    if request.method == 'GET':
        transformations = MOCK_TRANSFORMATION_DATA
        serializer = TransformationSerializer(transformations, many=True)
        return Response(serializer.data)

    # Create a transformation
    if request.method == 'POST':
        if list(filter(lambda x: x.name == request.data.get('name'), MOCK_TRANSFORMATION_DATA)):
            return Response(status=status.HTTP_409_CONFLICT)

        request.data['id'] = random.randint(10, 10000)
        serializer = TransformationSerializer(data=request.data)
        if serializer.is_valid():
            MOCK_TRANSFORMATION_DATA.append(Transformation(**serializer.data))
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def transformation_detail(request, name, format=None):
    global MOCK_TRANSFORMATION_DATA
    transformation = list(
        filter(lambda x: x.name == name, MOCK_TRANSFORMATION_DATA))

    if not transformation:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        transformation = transformation[0]

    # Retrieve a transformation
    if request.method == 'GET':
        serializer = TransformationSerializer(transformation)
        return Response(serializer.data)

    # Update a transformation
    elif request.method == 'PUT':
        team_object = transformation.__dict__
        team_object.update(request.data)
        serializer = TransformationSerializer(transformation, data=team_object)
        if serializer.is_valid():
            MOCK_TRANSFORMATION_DATA = list(
                filter(lambda x: x.name != name,  MOCK_TRANSFORMATION_DATA))
            MOCK_TRANSFORMATION_DATA.append(Transformation(**serializer.data))
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete a transformation
    elif request.method == 'DELETE':
        MOCK_TRANSFORMATION_DATA = list(
            filter(lambda x: x.name != name,  MOCK_TRANSFORMATION_DATA))
        return Response(status=status.HTTP_204_NO_CONTENT)
