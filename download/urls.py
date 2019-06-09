from django.urls import path
from . import views
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', views.field, name='field'),
    path('history', views.history),
    path('upload', views.upload),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
