from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo

from .seralizer import TodoSerializer

# Create your views here.


@api_view(['GET'])
def getallTodos(self , request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTodo(self , request):
    serializer = TodoSerializer(data=request.data)
    print("in add todo seralizer")
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
