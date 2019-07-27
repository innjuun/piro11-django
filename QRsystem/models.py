from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    usertime = models.DateTimeField(auto_now=True)

class QRcode(models.Model):
    url = models.CharField(max_length=100)