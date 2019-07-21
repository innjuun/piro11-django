from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # FIXME
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
