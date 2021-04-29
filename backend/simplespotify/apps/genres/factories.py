import factory
from factory.django import DjangoModelFactory

from .models import Genre


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(lambda n: f'Gernre__{n}')
