from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView)

from halls.forms import SearchForm, VideoForm
from halls.models import Hall, Video


def add_video(request, pk):
    """Add video to the exact hall."""
    form = VideoForm()
    search_form = SearchForm()
    hall = get_object_or_404(Hall, pk=pk)
    if not hall.user == request.user:
        raise PermissionDenied

    if request.method == 'POST':
        filled_form = VideoForm(request.POST)

        if filled_form.is_valid():
            video = Video()
            video.url = filled_form.cleaned_data.get('url')

            video.hall = hall
            video.save()
            return redirect('hall-detail', pk=pk)

    return render(
        request,
        'halls/add_video.html',
        {'form': form, 'search_form': search_form, 'hall': hall},
    )


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
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class HallCreateView(LoginRequiredMixin, CreateView):
    """Create Hall for an authenticated user."""

    model = Hall
    fields = ('title', )
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HallDetailView(DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'


class HallUpdateView(UpdateView):
    model = Hall
    fields = ('title', )
    template_name = 'halls/update_hall.html'
    success_url = reverse_lazy('dashboard')


class HallDeleteView(DeleteView):
    model = Hall
    template_name = 'halls/delete_hall.html'
    success_url = reverse_lazy('dashboard')
