import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) == 3


    def test_create(self):
        new_movie = {
            "title": "Йеллоустоун",
            "description": "Владелец ...",
            "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
            "year": 2018,
            "rating": 8.6,
            "genre_id": 17,
            "director_id": 1,
            "id": 1
        }
        movie = self.movie_service.create(new_movie)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        new_movie = {
            "title": "Омерзительная восьмерка",
            "description": "США после Гражданской войны...",
            "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
            "year": 2015,
            "rating": 7.8,
            "genre_id": 4,
            "director_id": 2,
            "id": 1
        }
        self.movie_service.update(new_movie)
