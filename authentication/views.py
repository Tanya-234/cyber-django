from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.views import LoginView,PasswordResetView, PasswordResetView

from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from authentication.models import User
from .forms import ProfileEditForm,LoginForm
from django.contrib.auth import views as auth_views

from .forms import CustomUserChangeForm, PasswordResetForm
from django.utils.translation import activate
from django.utils import translation
import logging
from django.http import HttpResponseRedirect
from django.conf import settings

logger = logging.getLogger(__name__)

class RegistrationView(CreateView):
    form_class = CustomUserChangeForm  # Use your custom form
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

    def form_valid(self, form):
        # Automatically log the user in after successful registration
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class HomeView(View):
    def get(self, request, *args, **kwargs):
    
      return render(request, 'home.html')

class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # Create an instance of the LoginForm and pass it to the template
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)  # Create a form instance with POST data

        if form.is_valid():
            # If the form is valid, extract the email and password
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Determine the user's language preference, for example, from their session
            user_language_preference = request.session.get('language_preference', 'en')

            # Set the user's language preference here
            request.LANGUAGE_CODE = user_language_preference

            # Authenticate the user
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Login was successful
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('incident_dashboard')  # Redirect to the incident dashboard
            else:
                # Authentication failed, display an error message
                messages.error(request, 'Login failed. Please check your email and password.')
        else:
            # Form is not valid, display an error message
            messages.error(request, 'Invalid form data. Please check your input.')

        # If login fails or form is invalid, render the login page again with the form
        return render(request, self.template_name, {'form': form})


class CustomLogoutView(auth_views.LogoutView):
    template_name = 'registration/logout.html'  
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'  # Optional: customize the email template
    success_url = reverse_lazy('password_reset_done')

    def get(self, request,*args, **kwargs):
        # form = PasswordResetForm(instance=request.user)
        return render(request, 'password_reset.html')
    
class ProfileView(View):
    template_name = 'profile.html'
    success_url = 'edit_profile'

    def get(self, request,*args, **kwargs):
        return render(request, 'profile.html')

class EditProfileView(View):
    template_name = 'edit_profile.html'
    
    def get(self, request, *args, **kwargs):
        form = ProfileEditForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, 'There was an error updating your profile.')
            return render(request, self.template_name, {'form': form})



def switch_language(request, language_code):
    next_url = request.GET.get('next', '/')
    print(f"Language Code: {language_code}")
    print(f"Next URL: {next_url}")

    if translation.check_for_language(language_code):
        translation.activate(language_code)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
    else:
        response = redirect(next_url)

    return response




