# freelancing/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, WorkRequest

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class WorkRequestForm(forms.ModelForm):
    class Meta:
        model = WorkRequest
        fields = ['title', 'description', 'assigned_to']
