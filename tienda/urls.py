from django.contrib import admin
from django.urls import path, include
from .views import index, productos

urlpatterns = [
    path('', index, name='index'),
    path('productos', productos, name='productos')
]
