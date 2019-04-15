from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Download
import youtube_dl
from .models import Data


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



"""\    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        download=False # We just want to extract the info
        )
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result
            print(video)
            video_url = video['link']
            print(video_url)
"""
