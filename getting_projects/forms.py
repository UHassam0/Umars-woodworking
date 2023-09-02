from .models import Project, Booking
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'public_visible', 'description', 'image')


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_subject', 'first_name', 'last_name', 'mobile_number',
                  'email_address', 'discussion_details', 'booking_date',
                  'booking_time')
        widgets = {
            "booking_date": DateInput(),
            "booking_time": TimeInput()
        }


class EdtBkngFrm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            "booking_date": DateInput(),
            "booking_time": TimeInput()
        }