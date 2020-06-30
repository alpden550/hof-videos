import urllib.parse


def parse_youtube_url(url):
    parsed_url = urllib.parse.urlparse(url)
    video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
    return video_id[0]
