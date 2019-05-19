from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

import youtube_dl
import os
import time
from .forms import Download
from .models import Data
from django.utils.timezone import now
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from youtubedl.settings import BASE_DIR
from validate_email import validate_email
from .tasks import get_audio, get_email

def val_email(email):
    return validate_email(email, verify = True)

def field(request):
    if request.method == 'POST':
        form = Download(request.POST)
        if form.is_valid():
            temp = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            get_audio(temp)
            get_email(email)
            return render(request, 'download/field.html', {'form': form})
    else:
        form = Download()
    return render(request, 'field.html', {'form': form})


def history(request):
    return render(request, 'history.html', {'options': Data.objects.all()})

def upload(request):
     file_dir = 'media/audio/{}'.format(x)
     print(file_dir, '\n\n\n')
     return render(request, 'upload.html', {'link': file_dir})
