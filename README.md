# HallOfFame for videos

Personal pages for user hall of fame videos.

## How to install

If poetry already installed run:

```bash
poetry install
```

If not, Should use a virtual environment for the best project isolation. Activate venv and install dependencies:

```bash
pip install -r requirements.txt
```

To get youtube api data got to [https://console.developers.google.com/](console.developers.google.com) and get YouTube API key (YouTube Data API v3)

Create .env and put into it:

```env
POSTGRES_DB= db name
POSTGRES_USER= db user
POSTGRES_PASSWORD= db password
POSTGRES_HOST=localhost (if run via docker)

SECRET_KEY= your secret key

YOUTUBE_API_KEY= your youtube api key

```

To start postgres locally run docker:

```sh
docker-compose up
```

## How to run

To run local

```bash
python manage.py migrate
python manage.py runserver
```
