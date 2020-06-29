from django import forms

from halls.models import Video


class VideoForm(forms.ModelForm):
    """Form to add video for a hall."""

    class Meta:
        model = Video
        fields = ('title', 'url', 'youtube_id')


class SearchForm(forms.Form):
    """Search video in the TouTube form."""

    search = forms.CharField(label='Searcg for Videos', max_length=255)
