from django import forms
from .models import Project,ProjectTeam


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'

class ProjectTeamCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields ='__all__'        
        
        
        