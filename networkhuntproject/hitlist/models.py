from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.
class HitlistPerson(models.Model):
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, null=True)
    position = models.CharField(
        max_length=255, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    twitter_url = models.URLField(max_length=255, blank=True, null=True)
    github_url = models.URLField(max_length=255, blank=True, null=True)
    portfolio_url = models.URLField(max_length=255, blank=True, null=True)
    profile_img = models.ImageField(
        null=True, blank=True, upload_to="static/job_tracker/images/hitlist")
    notes = HTMLField(blank=True, null=True)
    
    yes = 'Yes'
    no = 'No'
    coffee_chat_choices = [
        (yes, "YES"),
        (no, "NO"),
    ]
    coffee_chat = models.CharField(max_length=3, choices=coffee_chat_choices, null=False, default=no)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('hitlist')