import factory
from factory.django import DjangoModelFactory

from .models import Artist

class ArtistFactory(DjangoModelFactory):
    class Meta:
        model = Artist

    name = factory.Faker('name')
