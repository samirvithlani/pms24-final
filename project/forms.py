from django import forms
from .models import Project,ProjectTeam,Books


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'

class ProjectTeamCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields ='__all__'        
        
        
class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Books
        fields ='__all__'