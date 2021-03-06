from __future__ import unicode_literals
import time

from django.shortcuts import HttpResponse
from django.shortcuts import render
from validate_email import validate_email

from .forms import Download
from .models import GetFiles
from .tasks import get_audio, get_email

x = ''


def val_email(email):
    return validate_email(email, verify=True)


def field(request):
    if request.POST:
        form = Download(request.POST)
        if form.is_valid():
            temp = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            if not val_email(email):
                return HttpResponse('Your email is invalid')
            global x
            x = get_audio.delay(temp).get()
            get_email.delay(email)
    else:
        form = Download()

    return render(request, 'field.html', {'form': form})


def history(request):
    return render(request, 'history.html', {'options': GetFiles.objects.all()})


def upload(request):
    global x
    file_dir = 'media/audio/{}'.format(x)
    return render(request, 'upload.html', {'link': file_dir})
