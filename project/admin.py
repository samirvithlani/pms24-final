from django.contrib import admin
from .models import Project,Country,City

# Register your models here.
admin.site.register(Project)
admin.site.register(Country)
admin.site.register(City)