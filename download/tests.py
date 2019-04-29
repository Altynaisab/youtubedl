from django.test import TestCase
import youtube_dl
import os
from .views import getaudio

def getaudio(temp):
     ydl_opts = {
     'format': 'bestaudio/best',
     'postprocessors': [
     {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
      'preferredquality': '192',
     },
     {'key': 'FFmpegMetadata'},
         ],
                 }

    if x == 0:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(temp, download = False)
        else:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(temp)
     return meta['title']
