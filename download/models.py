from django.db import models
from django.conf import settings
from django.utils import timezone

class Data(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date')
    def __str__(self):
        return self.data_name
