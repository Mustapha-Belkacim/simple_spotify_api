import random

from django.core.management.base import BaseCommand, CommandError
from ....albums.factories import AlbumFactory
from ....genres.factories import GenreFactory
from ....artists.factories import ArtistFactory

class Command(BaseCommand):
    help = "Create albums with associated genres and artists"

    def add_arguments(self, parser):
        parser.add_argument('num_artists', nargs='?', type=int, help="number of artists to create")
        parser.add_argument('num_genres', nargs='?', type=int, help="number of genres to create")
        parser.add_argument('albums_per_genre', nargs='?', type=int, help="albums per genre")
        parser.add_argument('albums_per_artist', nargs='?', type=int, help="albums per artist")

    def handle(self, *args, **options):
        self.stdout.write("Creating data...")

        artists = []
        for _ in range(options['num_artists']):
            artists.append(ArtistFactory())

        genres = []
        for _ in range(options['num_genres']):
            genres.append(GenreFactory())

        for artist in artists:
            for _ in range(options['albums_per_artist']):
                AlbumFactory(artist=artist, genre=random.choice(genres))

        for genre in genres:
            for _ in range(options['albums_per_genre']):
                AlbumFactory(genre=genre, artist=random.choice(artists))
