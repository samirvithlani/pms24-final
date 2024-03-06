from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ProjectCreationForm
from .models import Project,ProjectTeam
from .forms import ProjectTeamCreationForm,BookCreationForm,TaskASignForm
from .models import City,Books,user_task,Task
from .models import User
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


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
    


def pieChart(request):
    labels = []
    data = []
    
    queryset = City.objects.order_by('-population')[:5]
    #[mumbai,tokio]
    #[100000,200000]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)
        
    return render(request, 'project/pie_chart.html',{
        'labels':labels,
        'data':data
    })        


class BookCreateView(CreateView):
    model = Books
    template_name = 'project/create_book.html'
    success_url = '/project/list/'
    form_class = BookCreationForm
        
class BookListView(ListView):
    template_name = 'project/book_list.html'
    model = Books
    context_object_name = 'books'        
  

class TaskASignView(CreateView):
    model = user_task
    template_name = 'project/task_assign.html'
    success_url = '/project/list/'
    form_class = TaskASignForm  
    

class TaskListView(ListView):
    template_name = 'project/task_list.html'
    model = Task
    context_object_name = 'tasks'   

class UpdateStatusView(View):
    
    def post(self,request,pk):
        print("UpdateStatusView")
        task = Task.objects.get(id=pk) #1    
         
        print("task..",task)
        task.status = "In Progress"
        print("task updated..")
        task.save()
        
        return redirect(reverse('task_list'))