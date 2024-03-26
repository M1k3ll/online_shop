from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
