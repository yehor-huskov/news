from django.db import models
from django.conf import settings
import datetime

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField()
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)
    approved = models.BooleanField(default=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
