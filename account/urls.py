from django.contrib import admin
from django.urls import path, include
from .views import register

urlpatterns = [

    
    path('', register,name = "registration")


]
