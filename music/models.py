from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=500)
    genre = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=1000)
