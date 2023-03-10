import pytest

from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        new_director = {
            "name": "New director name"
        }
        director = self.director_service.create(new_director)

        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        new_director = {
            "id": 1,
            "name": "Newest director name"
        }
        self.director_service.update(new_director)

