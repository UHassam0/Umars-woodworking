from .models import ExampleProject
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ExampleProject
        fields = ('project_name', 'public_visible', 'description', 'image')
