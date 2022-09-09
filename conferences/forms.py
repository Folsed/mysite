from .models import Conference
from django.forms import ModelForm, TextInput, DateTimeInput
from django import forms
from django_countries.widgets import CountrySelectWidget


class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = ['title', 'date', 'lat', 'lng', 'country']
        
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date',
                'type': 'datetime-local',
            }),
            'lat': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Latitude',
            }),
            'lng': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Longitude',
            }),
        }
        
