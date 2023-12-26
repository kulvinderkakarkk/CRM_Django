from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.redirect_home),
    path('login/', views.user_login, name='home.login'),
    path('logout/', views.user_logout, name='home.logout'),
    path('register/', views.user_register, name='home.register')
]