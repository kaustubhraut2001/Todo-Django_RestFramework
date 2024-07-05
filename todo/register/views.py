from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login

from .models import Register
from .serializer import RegisterSerializer

from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def registeration(request):
    data = request.data.copy()
    data['password'] = make_password(data['password'])
    serializer = RegisterSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login (request):
    username = request.data['username']
    password = request.data['password']
    print(username , password, "@@@@@@@@@")
    user = authenticate(request, username=username, password=password)
    print(user , "######")

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)



    

   