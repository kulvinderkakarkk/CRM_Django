from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('all/', views.allcustomers, name='customer.list')
]