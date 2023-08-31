from .models import ExampleProject
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ExampleProject
        fields = "__all__"

