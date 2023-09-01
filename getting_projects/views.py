from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Project, Booking
from .forms import ProjectForm, BookingForm


class Homepage(generic.ListView):
    model = Project
    queryset = Project.objects.filter(public_visible=True)
    template_name = "index.html"
    context_object_name = "projects"


class Projects(generic.ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = "projects"


class CreateProject(generic.CreateView):
    model = Project
    template_name = "create_project.html"
    form_class = ProjectForm
    success_url = reverse_lazy('manage')


class EditProject(generic.UpdateView):
    model = Project
    template_name = "edit_project.html"
    form_class = ProjectForm
    success_url = reverse_lazy('manage')


class DeleteProject(generic.DeleteView):
    model = Project
    template_name = "delete_project.html"
    success_url = reverse_lazy('manage')
    context_object_name = "project"


class Bookings(generic.ListView):
    model = Booking
    template_name = "bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user)


class CreateBooking(generic.CreateView):
    model = Booking
    template_name = "create_booking.html"
    form_class = BookingForm
    success_url = reverse_lazy('bookings')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)
