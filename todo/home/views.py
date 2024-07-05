from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import AllowAny
from .models import Todo
from .serializer import TodoSerializer

from django.contrib.auth.hashers import make_password


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def getallTodos(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def addTodo(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# suppoose we wnats to regisetr the user in the database
@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    data = request.data.copy()
    data['password'] = make_password(data['password'])
    serializer = TodoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete todo

@api_view(['DELETE'])
@permission_classes([AllowAny])
def deletetodo(request, todoid):

    queryset = Todo.objects.get(id=todoid)
    seralizer = TodoSerializer(queryset)
    queryset.delete()
    return Response( seralizer.data , status=status.HTTP_204_NO_CONTENT)


# updatetodo
@api_view(['PATCH'])
@permission_classes([AllowAny])
def updatetodo(request, todoid):
    try:
        queryset = Todo.objects.get(id=todoid)
    except Todo.DoesNotExist:
        raise "Not Found"

    serializer = TodoSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)