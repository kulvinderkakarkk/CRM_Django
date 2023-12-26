from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('all/', views.allcustomers, name='customer.list'),
    path('add/', views.AddCustomer, name='customer.add'),
    path('delete/<int:pk>', views.DeleteCustomer, name='customer.delete'),
    path('edit/<int:pk>', views.UpdateCustomer, name='customer.edit')
]