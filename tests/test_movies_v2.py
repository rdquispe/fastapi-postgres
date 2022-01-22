import pytest
from fastapi import status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

initial_movie_title = "Hello"
initial_movie_description = "World"
changed_movie_description = "From the other side"


class MoviesV2:

    @pytest.fixture
    def test_create_movie(request):
        """This fixture will only be available within the scope of TestGroup"""
        response = client.post(
            "/movies/create",
            json={"title": initial_movie_title, "description": initial_movie_description},
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["title"] == "Hello"
        assert response.json()["description"] == "World"
        request.config.cache.set("movie_id", response.json()["id"])
