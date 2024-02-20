from django.contrib import admin
from django.urls import path, include
from .views import ProjectCreationView,ProjectListView

urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="project_create"),
 path("list/",ProjectListView.as_view(),name="project_list"),
]