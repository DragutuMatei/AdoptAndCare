from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from animals.models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'email', 'id': 'email', 'placeholder': 'Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'email', 'id': 'username', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password', 'class': 'password', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password2', 'class': 'password', 'placeholder': 'Reenter the password'}))

    class Meta:
        model = User
        fields = ("username", 'email', "password1", "password2")


class EditUserView(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'email', 'id': 'username', 'placeholder': "Enter the your username"}),
            'first_name': forms.TextInput(attrs={'class': 'email', 'id': 'email', 'placeholder': "Enter the your first name"}),
            'last_name': forms.TextInput(attrs={'class': 'password', 'id': 'password', 'placeholder': "Enter the your last name"}),
            'email': forms.EmailInput(attrs={'class': 'password', 'id': 'password2', 'placeholder': "Enter the your email"}),
        }


class ProfileForm(forms.ModelForm):
    adresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your adress(Country, County, City)'})),
    imag = forms.ImageField(widget=forms.TextInput(attrs={'id': 'inputFile'})),
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})),
    media = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your facebook'})),
    
    class Meta:
        model = Profile
        fields = ('adresa', 'imag', 'phone', 'media')









