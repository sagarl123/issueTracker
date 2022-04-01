from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic import CreateView 
from .forms import CustomUserCreationForm 
from django.urls import reverse_lazy
from .models import CustomUser 
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    