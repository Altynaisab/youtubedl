from django.shortcuts import render
from django.http import HttpResponse


def field(request):
    return render(request, 'field.html', {})
