from django.urls import path
from . import views

urlpatterns = [
    path('', views.field, name = 'field'),
    path('history', views.history)
    
    ]
