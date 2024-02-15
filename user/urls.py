from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path("manager-register/",views.ManagerRegisterView.as_view(),name="manager-register"),
]