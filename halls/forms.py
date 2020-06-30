from django import forms

from halls.models import Video
from halls.youtube import get_yotube_title, parse_youtube_url


class VideoForm(forms.ModelForm):
    """Form to add video for a hall."""

    class Meta:
        model = Video
        fields = ('url', )
        labels = {'url': 'YouTube URL'}
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        url = self.cleaned_data['url']
        if parse_youtube_url(url) is None:
            raise forms.ValidationError('Needs to be the valid YouTube video URL')

        video_id = parse_youtube_url(url)
        if get_yotube_title(video_id) is None:
            raise forms.ValidationError('Needs to be the valid YouTube video URL')


class SearchForm(forms.Form):
    """Search video in the TouTube form."""

    search = forms.CharField(label='Search for Videos', max_length=255)
