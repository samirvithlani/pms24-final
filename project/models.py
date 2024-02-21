from django.db import models
from user.models import User

# Create your models here.
techChoices = (
("Python","Python"),
("Java","Java"),
("C++","C++"),
("C#","C#"),
)
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100,choices=techChoices)
    estimated_hours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    
    
    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.name    

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)        
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "projectteam"
    
    def __str__(self):
        return self.user.username    
    