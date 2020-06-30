import urllib.parse
import requests
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/videos'


def parse_youtube_url(url):
    parsed_url = urllib.parse.urlparse(url)
    video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
    return video_id[0]


def get_yotube_title(video_id):
    payload = {
        'part': 'snippet',
        'id': video_id,
        'key': YOUTUBE_API_KEY,
    }

    response = requests.get(YOUTUBE_URL, params=payload)
    response.raise_for_status()
    return response.json().get('items')[0]['snippet']['title']
