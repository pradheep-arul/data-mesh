from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (MOCK_DAG_BACKFILL_DATA, MOCK_DAG_DATA,
                     MOCK_DAG_TRIGGER_DATA)


@api_view(['GET'])
def dag_list(request, format=None):
    # Retrieve all DAGs
    if request.method == 'GET':
        return Response(MOCK_DAG_DATA, status=status.HTTP_200_OK)


@api_view(['GET'])
def dag_detail(request, name, format=None):
    # Retrieve a DAG
    if request.method == 'GET':
        return Response(MOCK_DAG_DATA[0], status=status.HTTP_200_OK)


@api_view(['POST'])
def dag_trigger(request, name, format=None):
    # Trigger a DAG
    if request.method == 'POST':
        return Response(MOCK_DAG_TRIGGER_DATA, status=status.HTTP_200_OK)


@api_view(['POST'])
def dag_backfill(request, name, format=None):
    # Backfill a DAG
    if request.method == 'POST':
        return Response(MOCK_DAG_BACKFILL_DATA, status=status.HTTP_200_OK)
