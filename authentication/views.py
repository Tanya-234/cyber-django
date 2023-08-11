from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegistrationView(CreateView):
    form_class = UserCreationForm  # Use the default user creation form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('registration/login')  # Redirect to login page after successful registration

    def form_valid(self, form):
        # Automatically log the user in after successful registration
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
    
class LoginView(View):
    def get( self,request,*args, **kwargs):
        return render(request, 'login.html')
    
class LogoutView(View):
    def get( self,request,*args, **kwargs):
        return render(request, 'logout.html')
    
   
   