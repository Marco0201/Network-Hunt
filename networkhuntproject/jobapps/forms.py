from django import forms
from bootstrap_datepicker_plus.widgets import *
from tinymce.widgets import TinyMCE 
from .models import *


class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False

class PostJobForm(forms.ModelForm):
    class Meta:
        model = Job_application
        fields = ('user', 'position', 'pay', 'company',
                  'employee', 'job_board', 'job_url', 'have_you_applied','date_applied', 'notes')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'pay': forms.NumberInput(attrs={'class': 'form-control'}),
            'employee': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'job_board': forms.TextInput(attrs={'class': 'form-control'}),
            'job_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://indeed.com'}),
            'have_you_applied': forms.Select(attrs={'class': 'form-control'}),
            'date_applied': DatePickerInput(options={"format": "MM/DD/YYYY"}),
            'notes': TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10}),
        }


class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job_application
        fields = ('user', 'position', 'pay', 'company',
                  'employee', 'job_board', 'job_url', 'have_you_applied', 'date_applied', 'notes')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'pay': forms.NumberInput(attrs={'class': 'form-control'}),
            'employee': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'job_board': forms.TextInput(attrs={'class': 'form-control'}),
            'job_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://indeed.com'}),
            'have_you_applied': forms.Select(attrs={'class': 'form-control'}),
            'date_applied': DatePickerInput(options={"format": "MM/DD/YYYY"}),
            'notes': TinyMCEWidget( 
            attrs={'required': False, 'cols': 30, 'rows': 10}),
        }
