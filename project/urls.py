from django.contrib import admin
from django.urls import path, include
from views import ProjectCreationView

urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="create"),
]