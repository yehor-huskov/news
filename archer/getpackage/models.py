from django.db import models
from django.conf import settings
import datetime


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)
    approved = models.BooleanField()
