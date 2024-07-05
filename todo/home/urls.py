from django.contrib import admin
from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('getall/', views.getallTodos, name='getallTodos'),
    path('add/', views.addTodo, name='addTodo'),
    path('register/' , views.registerUser, name='registerUser'),
    path('deletetodo/<int:todoid>', views.deletetodo, name='deletetodo'),
    path('updatetodo/<int:todoid>', views.updatetodo, name='updatetodo'),
]