from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

from halls.models import Hall


class HallMainPage(TemplateView):
    """View to represent main page."""

    template_name = 'halls/index.html'


class DashboardView(TemplateView):
    """View for an user dashboard."""

    template_name = 'halls/dashboard.html'


class UserSignUpView(CreateView):
    """Sign up an user."""

    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Login a new creating user."""
        view = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class HallCreateView(LoginRequiredMixin, CreateView):
    """Create Hall for an authenticated user."""

    model = Hall
    fields = ('title', )
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HallDetailView(DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'
