from django import forms
from django.contrib.auth.models import User
from .models import *


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_from', 'message']
        widgets = {
            'email_from':forms.TextInput(attrs={"placeholder":"Enter your email*"}),
            'message':forms.Textarea(attrs={"placeholder":"Write your message*"})
        }

class CreatePetForm(forms.ModelForm):
    class Meta():
        model = Pet
        fields = ('name', 'description', 'imag1', 'imag2', 'imag3', 'imag4', 'imag5', 'animal', 'age', 'de_rasa', 'take_care', 'size', 'gender', 'condition')

    