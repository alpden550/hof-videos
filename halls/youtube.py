import os
import urllib.parse

import requests

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/videos'
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'


def parse_youtube_url(url):
    parsed_url = urllib.parse.urlparse(url)
    video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
    return video_id


def get_yotube_title(video_id):
    payload = {
        'part': 'snippet',
        'id': video_id,
        'key': YOUTUBE_API_KEY,
    }

    response = requests.get(YOUTUBE_URL, params=payload)
    response.raise_for_status()
    video_json = response.json().get('items')
    if video_json:
        return video_json[0]['snippet']['title']


def search_videos_in_youtube(text, limit=6):
    encoded_text = urllib.parse.quote(text)
    payload = {
        'part': 'snippet',
        'key': YOUTUBE_API_KEY,
        'maxResults': limit,
        'q': encoded_text,
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params=payload)
    response.raise_for_status()
    return response.json()
