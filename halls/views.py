from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class HallMainPage(TemplateView):
    """View to represent main page."""

    template_name = 'halls/index.html'


class UserSignUpView(CreateView):
    """Sign up an user."""

    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
