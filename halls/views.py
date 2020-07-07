from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from halls.forms import SearchForm, VideoForm
from halls.models import Hall, Video
from halls.youtube import (get_yotube_title, parse_youtube_url,
                           search_videos_in_youtube)


def add_video(request, pk):
    """Add video to the exact hall."""
    search_form = SearchForm()
    hall = get_object_or_404(Hall, pk=pk)
    if not hall.user == request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():
            video = Video()
            video.url = form.cleaned_data.get('url')
            video_id = parse_youtube_url(video.url)[0]
            if video_id:
                video.hall = hall
                video.youtube_id = video_id
                video.title = get_yotube_title(video_id)
                video.save()
                return redirect('hall-detail', pk=pk)
    else:
        form = VideoForm()

    return render(
        request,
        'halls/add_video.html',
        {'search_form': search_form, 'hall': hall, 'form': form},
    )


def video_search(request):
    """Return finding videos form searcg form."""
    form = SearchForm(request.GET)

    if form.is_valid():
        search_text = form.cleaned_data.get('search')
        videos = search_videos_in_youtube(search_text)

        return JsonResponse(videos)

    return JsonResponse({'error': 'Not able to validate form.'})


class VideoDeleteView(DeleteView):
    """Delete video."""

    model = Video
    template_name = 'halls/delete_video.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        video = self.get_object()
        if video.hall.user != request.user:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


class HallMainPage(ListView):
    """View to represent main page."""

    template_name = 'halls/index.html'
    queryset = Hall.objects.all().order_by('-id')[:3]
    context_object_name = 'halls'


class DashboardView(ListView):
    """View for an user dashboard."""

    template_name = 'halls/dashboard.html'
    model = Hall
    context_object_name = 'halls'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).prefetch_related('videos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            raise PermissionDenied

        return context


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
