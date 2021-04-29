from django.db import models

from ..genres.models import Genre
from ..artists.models import Artist

class Album(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, related_name='albums', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
