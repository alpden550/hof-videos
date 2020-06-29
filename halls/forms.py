from django import forms

from halls.models import Video


class VideoForm(forms.ModelForm):
    """Form to add video for a hall."""

    class Meta:
        model = Video
        fields = ('title', 'url', 'youtube_id')
