from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo

from .serializer import TodoSerializer

# Create your views here.


@api_view(['GET'])
def getallTodos( request):
    # todos = Todo.objects.all()
    # serializer = TodoSerializer(todos, many=True)
    # return Response(serializer.data)
    return "Hello"

@api_view(['POST'])
def addTodo( request):
    serializer = TodoSerializer(data=request.data)
    print("in add todo seralizer")
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
