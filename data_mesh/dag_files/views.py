
from ..dags.models import MOCK_DAG_DATA
from .models import MOCK_DAGS_FILES_DATA
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def file_list(request, format=None):
    # Retrieve all file details
    if request.method == 'GET':
        return Response(MOCK_DAGS_FILES_DATA, status=status.HTTP_200_OK)

    # Upload a file
    if request.method == 'POST':
        data = MOCK_DAGS_FILES_DATA[0].copy()
        data['dags'] = MOCK_DAG_DATA
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def file_detail(request, name, format=None):
    # Retrieve a file detail
    if request.method == 'GET':
        data = MOCK_DAGS_FILES_DATA[0].copy()
        data['dags'] = MOCK_DAG_DATA
        return Response(data, status=status.HTTP_200_OK)

    # Replace a file
    if request.method == 'PUT':
        data = MOCK_DAGS_FILES_DATA[0].copy()
        data['dags'] = MOCK_DAG_DATA
        return Response(data, status=status.HTTP_200_OK)

    # Delete a file
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def file_download(request, name, format=None):

    # Download a file
    if request.method == 'GET':
        response = HttpResponse(open('storage/dags/intercom-import.py',
                                'rb').read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="intercom-import.py"'
        return response
