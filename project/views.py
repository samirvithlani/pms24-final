from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ProjectCreationForm
from .models import Project,ProjectTeam
from .forms import ProjectTeamCreationForm,BookCreationForm
from .models import City,Books

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