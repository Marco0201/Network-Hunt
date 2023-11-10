from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
# Create your models here.


class Job_application(models.Model):
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=255)
    pay = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=255)
    employee = models.CharField(
        max_length=255, blank=True, null=True)
    job_board = models.CharField(max_length=255)
    job_url = models.URLField(max_length=255)
    notes = HTMLField(blank=True, null=True)

    yes = 'Yes'
    no = 'No'
    have_you_applied_choices = [
        (yes, "YES"),
        (no, "NO"),
    ]

    have_you_applied = models.CharField(max_length=3, choices=have_you_applied_choices, null=False, default=no)
    date_applied = models.DateField(auto_created=False)

    def __str__(self):
        return self.position
    
    def get_absolute_url(self):
        return reverse('home')
