from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import ExampleProject


class Homepage(generic.ListView):
    model = ExampleProject
    queryset = ExampleProject.objects.filter(public_visible=True)
    template_name = "index.html"
    context_object_name = "example_projects"


class Projects(generic.ListView):
    model = ExampleProject
    template_name = "projects.html"
    context_object_name = "projects"

class CreateProject(generic.CreateView):
    model = ExampleProject
    fields = __all__
