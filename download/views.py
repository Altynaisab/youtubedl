from __future__ import unicode_literals

from django.shortcuts import render

from .forms import Download
from .models import Data
from .tasks import get_audio, get_email

def val_email(email):
    return validate_email(email, verify=True)

def field(request):
    if request.method == 'POST':
        form = Download(request.POST)
        if form.is_valid():
            temp = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
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
