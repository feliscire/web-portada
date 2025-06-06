from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']  # o puedes usar una tupla: ('created', 'updated')

admin.site.register(Project, ProjectAdmin)