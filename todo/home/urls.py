from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('all/',  views.getallTodos ),
    path('add/', views.addTodo ),
]
