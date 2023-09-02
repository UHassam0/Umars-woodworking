from django.contrib import admin
from .models import Project, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('project_name', 'description',
                    'public_visible', 'updated_on')
    search_fields = ['project_name', 'description']
    list_filter = ('public_visible', 'updated_on')
    summernote_fields = ('description',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'first_name', 'last_name', 'email_address',
                    'booking_date', 'booking_time', 'discussion_details',
                    'booking_subject')
    search_fields = ['booking_subject', 'discussion_details', 'first_name',
                     'last_name']
    list_filter = ('booking_date', 'client')
    summernote_fields = ('booking_description',)
