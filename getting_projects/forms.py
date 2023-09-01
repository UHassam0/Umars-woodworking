from .models import Project, Booking
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'public_visible', 'description', 'image')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_subject', 'discussion_details', 'booking_date', 'booking_time')