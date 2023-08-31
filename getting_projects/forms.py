from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'public_visible', 'description', 'image')
