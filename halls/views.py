from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from halls.models import Hall


class HallMainPage(TemplateView):
    """View to represent main page."""

    template_name = 'halls/index.html'


class UserSignUpView(CreateView):
    """Sign up an user."""

    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')


class HallCreateView(LoginRequiredMixin, CreateView):
    model = Hall
    fields = ('title', )
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
