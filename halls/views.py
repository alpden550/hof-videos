from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from halls.forms import SearchForm, VideoForm, HallFormset
from halls.models import Hall, Video
from halls.youtube import (get_yotube_title, parse_youtube_url,
                           search_videos_in_youtube)


@login_required
def add_video(request, pk):
    """Add video to the exact hall."""
    search_form = SearchForm()
    hall = get_object_or_404(Hall, pk=pk)
    if not hall.user == request.user:
        raise Http404

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
                return redirect('hall:hall-detail', pk=pk)
    else:
        form = VideoForm()

    return render(
        request,
        'halls/add_video.html',
        {'search_form': search_form, 'hall': hall, 'form': form},
    )


@login_required
def video_search(request):
    """Return finding videos form searcg form."""
    form = SearchForm(request.GET)

    if form.is_valid():
        search_text = form.cleaned_data.get('search')
        videos = search_videos_in_youtube(search_text)

        return JsonResponse(videos)

    return JsonResponse({'error': 'Not able to validate form.'})


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    """Delete video."""

    model = Video
    template_name = 'halls/delete_video.html'
    success_url = reverse_lazy('hall:dashboard')

    def get_object(self):
        video = super().get_object()
        if video.hall.user != self.request.user:
            raise Http404
        return video


class HallMainPage(ListView):
    """View to represent main page."""

    template_name = 'halls/index.html'
    queryset = Hall.objects.all().order_by('-id')[:5]
    context_object_name = 'halls'


class DashboardView(LoginRequiredMixin, ListView):
    """View for an user dashboard."""

    template_name = 'halls/dashboard.html'
    model = Hall
    context_object_name = 'halls'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).prefetch_related('videos')


class HallCreateView(LoginRequiredMixin, CreateView):
    """Create Hall for an authenticated user."""

    model = Hall
    fields = ('title', )
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('hall:dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = HallFormset(queryset=Hall.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        formset = HallFormset(request.POST, request.FILES)

        if formset.is_valid():
            for form in formset:
                form.instance.user = self.request.user
            formset.save()
            return redirect('hall:dashboard')
        else:
            return self.form_invalid(formset)

    def form_invalid(self, formset):
        return self.render_to_response(self.get_context_data(formset=formset))


class HallDetailView(DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'


class HallUpdateView(LoginRequiredMixin, UpdateView):
    model = Hall
    fields = ('title', )
    template_name = 'halls/update_hall.html'
    success_url = reverse_lazy('hall:dashboard')

    def get_object(self):
        hall = super().get_object()
        if hall.user != self.request.user:
            raise Http404
        return hall


class HallDeleteView(LoginRequiredMixin, DeleteView):
    model = Hall
    template_name = 'halls/delete_hall.html'
    success_url = reverse_lazy('hall:dashboard')

    def get_object(self):
        hall = super().get_object()
        if hall.user != self.request.user:
            raise Http404
        return hall
