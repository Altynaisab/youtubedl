from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def field(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'download/field.html', {})
