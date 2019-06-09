from django.test import TestCase
from .views import get_email
from .views import val_email
import youtube_dl
import os
from youtubedl.settings import BASE_DIR

def get_audio(temp, x):
    ydl_opts = {
        'keepvideo': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': './audio/%(title)s.mp3',
    }

    if x == 0:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                temp, download=False,
            )
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                temp
            )
    return meta['title']
