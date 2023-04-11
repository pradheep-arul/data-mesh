import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MOCK_TEAM_DATA, Team
from .serializers import TeamSerializer


@api_view(['GET', 'POST'])
def team_list(request, format=None):
    # Retrieve all teams
    if request.method == 'GET':
        teams = MOCK_TEAM_DATA
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    # Create a team
    if request.method == 'POST':
        if list(filter(lambda x: x.name == request.data.get('name'), MOCK_TEAM_DATA)):
            return Response(status=status.HTTP_409_CONFLICT)

        request.data['id'] = random.randint(10, 10000)
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            MOCK_TEAM_DATA.append(Team(**serializer.data))
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, name, format=None):
    global MOCK_TEAM_DATA
    team = list(filter(lambda x: x.name == name, MOCK_TEAM_DATA))

    if not team:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        team = team[0]

    # Retrieve a team
    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a team
    elif request.method == 'PUT':
        team_object = team.__dict__
        team_object.update(request.data)
        serializer = TeamSerializer(team, data=team_object)
        if serializer.is_valid():
            MOCK_TEAM_DATA = list(
                filter(lambda x: x.name != name,  MOCK_TEAM_DATA))
            MOCK_TEAM_DATA.append(Team(**serializer.data))
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete a team
    elif request.method == 'DELETE':
        MOCK_TEAM_DATA = list(
            filter(lambda x: x.name != name,  MOCK_TEAM_DATA))
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def member_list(request, name, format=None):
    global MOCK_TEAM_DATA
    team = list(filter(lambda x: x.name == name, MOCK_TEAM_DATA))

    if not team:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        team = team[0]

    # Add member to a team
    if request.method == 'POST':
        member = request.data.get('member')
        if member in team.members:
            return Response(status=status.HTTP_409_CONFLICT)

        team.members.append(member)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)


@ api_view(['DELETE'])
def member_detail(request, name, member, format=None):
    global MOCK_TEAM_DATA
    team = list(filter(lambda x: x.name == name, MOCK_TEAM_DATA))

    if not team:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        team = team[0]

    # Remove member to a team
    if request.method == 'DELETE':
        if member not in team.members:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        team.members.remove(member)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)
