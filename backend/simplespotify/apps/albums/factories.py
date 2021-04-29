import factory
from factory.django import DjangoModelFactory

from .models import Album
from ..artists.factories import ArtistFactory
from ..genres.factories import GenreFactory

class AlbumFactory(DjangoModelFactory):
    class Meta:
        model = Album

    name = factory.Sequence(lambda n: f'album__{n}')
    artist = factory.SubFactory(ArtistFactory)
    genre = factory.SubFactory(GenreFactory)
