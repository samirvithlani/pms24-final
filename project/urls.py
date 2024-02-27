from django.contrib import admin
from django.urls import path, include
from .views import ProjectCreationView,ProjectListView,ProjectTeamCreateView
from .import views

urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="project_create"),
 path("list/",ProjectListView.as_view(),name="project_list"),
 path("create_team/",ProjectTeamCreateView.as_view(),name="project_team_create"),
 path ("chart/",views.pieChart,name="chart")
]