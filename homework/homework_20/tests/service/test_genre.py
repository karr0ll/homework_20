import pytest

from service.genre import GenreService
from tests.conftest import genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        new_genre = {
            "name": "New genre name"
        }
        genre = self.genre_service.create(new_genre)

        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        new_genre = {
            "id": 1,
            "name": "Newest genre name"
        }
        self.genre_service.update(new_genre)

