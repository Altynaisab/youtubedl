from celery.decorators import task
import youtube_dl
import os
from youtubedl.settings import BASE_DIR
from config.celery import app
from .models import Data
from django.core.mail import EmailMessage
from validate_email import validate_email
from django.utils.timezone import now

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost')

@app.task
def get_audio(temp):
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [
    {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
     'preferredquality': '192',
    },
    {'key': 'FFmpegMetadata'},
        ],
        'outtmpl': 'media/audio/%(title)s.mp3',
            }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(temp)

    Data.objects.create(name=meta['title'], pub_date = now())
    return meta['title']


@app.task
def get_email(email, file):
    msg = EmailMessage('mp3-converter', 'http://127.0.0.1:8000/youtubedl/download/upload', to=[email])
    msg.send()
    return render(request, 'upload.html',  {'link': file_dir})
