from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm
from django import forms

class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Add more fields if needed

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Replace with your User model
        fields = ['username', 'email', 'first_name', 'last_name']  # Include the fields you want to edit
