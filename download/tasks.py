import youtube_dl
from celery import Celery
from django.core.mail import EmailMessage
from django.utils.timezone import now

from .models import Data

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost')

@app.task
def get_audio(temp):
    options = {
        'extractaudio': True,
        'audioformat': "mp3",
        'outtmpl': 'media/%(id)s',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        meta = ydl.extract_info(temp, download=True)

    Data.objects.create(name=meta['title'], pub_date=now())
    return meta['title']


@app.task
def get_email(email, file):
    msg = EmailMessage('mp3-converter', 'http://127.0.0.1:8000/youtubedl/download/upload', to=[email])
    msg.send()
    return render(request, 'upload.html', {'link': file_dir})
