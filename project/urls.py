from django.contrib import admin
from django.urls import path, include
from .views import ProjectCreationView,ProjectListView,ProjectTeamCreateView,BookCreateView,TaskASignView,TaskListView,UpdateStatusView
from .import views

urlpatterns = [
 
 path("create/",ProjectCreationView.as_view(),name="project_create"),
 path("list/",ProjectListView.as_view(),name="project_list"),
 path("create_team/",ProjectTeamCreateView.as_view(),name="project_team_create"),
 path ("chart/",views.pieChart,name="chart"),
 path("book_create/",BookCreateView.as_view(),name="book_create"),
 path("book_list/",views.BookListView.as_view(),name="book_list"),
 path("task_assign/",views.TaskASignView.as_view(),name="task_assign"),
 path("task_list/",views.TaskListView.as_view(),name="task_list"),
 path("task_update/<int:pk>/",views.UpdateStatusView.as_view(),name="update_status"),
 
]