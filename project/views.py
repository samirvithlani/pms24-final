from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ProjectCreationForm
from .models import Project,ProjectTeam
from .forms import ProjectTeamCreationForm

# Create your views here.

class ProjectCreationView(CreateView):
    template_name = 'project/create.html'
    model = Project
    form_class = ProjectCreationForm
    success_url = '/project/list/'
    
    

class ProjectListView(ListView):
    template_name = 'project/list.html'
    model = Project
    context_object_name = 'projects'


class ProjectTeamCreateView(CreateView):    
    template_name = 'project/create_team.html'
    model = ProjectTeam
    success_url = '/project/list/'
    form_class = ProjectTeamCreationForm
    