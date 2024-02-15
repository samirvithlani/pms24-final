from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegistrationForm, DeveloperRegistrationForm

# Create your views here.
class ManagerRegisterView(CreateView):
    template_name = 'user/manage_register.html'
    model = User
    form_class = ManagerRegistrationForm
    success_url = '/login/'


class DeveloperRegisterView(CreateView):
    template_name = 'user/developer_register.html'
    model = User
    form_class = DeveloperRegistrationForm
    success_url = '/login/'    