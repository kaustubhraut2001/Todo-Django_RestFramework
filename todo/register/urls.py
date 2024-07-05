from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('registeration/' , views.registeration, name='registerUser'),
    path('login/' , views.login, name='loginUser'),
]