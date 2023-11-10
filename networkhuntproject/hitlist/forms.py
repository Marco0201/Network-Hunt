from django import forms
from tinymce.widgets import TinyMCE 
from .models import *

class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False


class HitlistForm(forms.ModelForm):
    class Meta:
        model = HitlistPerson
        fields = ('user', 'name', 'email', 'company', 'position', 'coffee_chat', 'linkedin_url', 
                  'twitter_url', 'github_url', 'portfolio_url', 'profile_img', 'notes')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'coffee_chat': forms.Select(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://indeed.com/user110'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://indeed.com/user110'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/user110'}),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://usersite.com'}),
            'profile_img': forms.FileInput(attrs={'class': 'form-control'}),
            'notes': TinyMCEWidget( attrs={'required': False, 'cols': 30, 'rows': 10}),
        }


class EditHitlist(forms.ModelForm):
    class Meta:
        model = HitlistPerson
        fields = ('user', 'name', 'email', 'company', 'position',  'coffee_chat','linkedin_url', 
                  'twitter_url', 'github_url', 'portfolio_url', 'profile_img', 'notes')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'coffee_chat': forms.Select(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://indeed.com/user110'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://indeed.com/user110'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/user110'}),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://usersite.com'}),
            'profile_img': forms.FileInput(attrs={'class': 'form-control'}),
            'notes': TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10}),
        }
