
from .models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'contact_details', 'password']
        widgets = {'password': forms.PasswordInput()}  # Add a password input widget


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'contact_details','first_name', 'last_name'] # Include the fields you want to edit

class PasswordResetForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']


class LoginForm(forms.Form):
    email = forms.EmailField(label=_("Email"))
    password = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
