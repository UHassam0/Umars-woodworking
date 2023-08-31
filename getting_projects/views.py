from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from .models import ExampleProject
from .forms import ProjectForm


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
    template_name = "createproject.html"
    form_class = ProjectForm
    success_url = reverse_lazy('manage')


class EditProject(generic.UpdateView):
    model = ExampleProject
    template_name = "editproject.html"
    form_class = ProjectForm
    success_url = reverse_lazy('manage')


class DeleteProject(generic.DeleteView):
    model = ExampleProject
    template_name = "deleteproject.html"
    success_url = reverse_lazy('manage')
    context_object_name = "project"
