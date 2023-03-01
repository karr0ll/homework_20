from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director1 = Director(id=1, name="Directors name 1")
    director2 = Director(id=2, name="Directors name 2")
    director3 = Director(id=3, name="Directors name 3")

    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2, director3])
    director_dao.create = MagicMock(return_value=Director(id=4))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock(return_value=director1)

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name="genres name 1")
    genre2 = Genre(id=2, name="genres name 2")
    genre3 = Genre(id=3, name="genres name 3")

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=4))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock(return_value=genre1)

    return genre_dao

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(
        id=1,
        title="title name 1",
        description="description 1",
        trailer="trailer link 1",
        year=2010,
        rating=7.77,
        genre_id=1,
        director_id=2
    )
    movie2 = Movie(
        id=2,
        title="title name 2",
        description="description 2",
        trailer="trailer link 2",
        year=2011,
        rating=8.88,
        genre_id=2,
        director_id=3
    )
    movie3 = Movie(
        id=3,
        title="title name 3",
        description="description 3",
        trailer="trailer link 3",
        year=2013,
        rating=9.99,
        genre_id=3,
        director_id=4
    )

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock(return_value=movie1)

    return movie_dao
