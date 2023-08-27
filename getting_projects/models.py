from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ExampleProject(models.Model):
    project_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    public_visible = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.project_name


class Booking(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    discussion_details = models.TextField()
    booking_subject = models.CharField(max_length=200)
