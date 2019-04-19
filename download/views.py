from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Download
import youtube_dl
from .models import Data
from django.utils.timezone import now

def field(request):
    if request.method == 'POST':
        form = Download(request.POST)
        if form.is_valid():
            link = form.cleaned_data
            ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
             'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
                ],
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link['link']])

    else:
        form = Download()

    return render(request, 'field.html', {'form': form})

def history(request):
    return render(request, 'history.html', {'options' : Data.objects.all()})
