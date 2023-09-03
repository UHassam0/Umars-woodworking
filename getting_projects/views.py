from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Project, Booking
from .forms import ProjectForm, BookingForm, EdtBkngFrm
from datetime import date


class Homepage(generic.ListView):
    model = Project
    queryset = Project.objects.filter(public_visible=True)
    template_name = "index.html"
    context_object_name = "projects"


class Projects(generic.ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = "projects"


class CreateProject(SuccessMessageMixin, generic.CreateView):
    model = Project
    template_name = "create_project.html"
    form_class = ProjectForm
    success_url = reverse_lazy('manage')
    success_message = "%(project_name)s was created successfully"


class EditProject(SuccessMessageMixin, generic.UpdateView):
    model = Project
    template_name = "edit_project.html"
    form_class = ProjectForm
    success_url = reverse_lazy('manage')
    success_message = "%(project_name)s was updated successfully"


class DeleteProject(SuccessMessageMixin, generic.DeleteView):
    model = Project
    template_name = "delete_project.html"
    success_url = reverse_lazy('manage')
    context_object_name = "project"
    success_message = "%(project_name)s was deleted successfully"


class Bookings(generic.ListView):
    model = Booking
    template_name = "bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user)


class CreateBooking(SuccessMessageMixin, generic.CreateView):
    model = Booking
    template_name = "create_booking.html"
    form_class = BookingForm
    success_url = reverse_lazy('bookings')
    success_message = "%(booking_subject)s was created successfully"

    def form_valid(self, form):
        if self is not None:
            form.instance.client = self.request.user
            return super().form_valid(form)


class ReviewBookings(generic.ListView):
    model = Booking
    template_name = "upcoming_bookings.html"
    context_object_name = "bookings"
    queryset = Booking.objects.filter(booking_date__gte=date.today())


class EditBooking(SuccessMessageMixin, generic.UpdateView):
    model = Booking
    template_name = "edit_booking.html"
    context_object_name = 'booking'
    success_url = reverse_lazy('rev_bk')
    success_message = "%(booking_subject)s was edited successfully"
    form_class = EdtBkngFrm
