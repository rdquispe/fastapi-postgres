import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

initial_movie_title = "Hello"
initial_movie_description = "World"
changed_movie_description = "From the other side"


@pytest.mark.dependency()
def test_create_movie(request):
    response = client.post(
        "/movies/create",
        json={"title": initial_movie_title, "description": initial_movie_description},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["title"] == "Hello"
    assert response.json()["description"] == "World"
    request.config.cache.set("movie_id", response.json()["id"])


@pytest.mark.dependency(depends=["test_create_movie"])
def test_get_all_movies():
    response = client.get("/movies/list/all")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None


@pytest.mark.dependency(depends=["test_create_movie"])
def test_get_one_movie(request):
    movie_id = request.config.cache.get("movie_id", None)
    response = client.get(f"/movies/get/{movie_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == movie_id
    assert response.json()["title"] == initial_movie_title
    assert (
            response.json()["description"] == initial_movie_description
            or changed_movie_description
    )


@pytest.mark.dependency(depends=["test_create_movie", "test_get_one_movie"])
def test_patch_movie(request):
    movie_id = request.config.cache.get("movie_id", None)
    response = client.patch(
        "/movies/update",
        json={
            "id": movie_id,
            "title": initial_movie_title,
            "description": changed_movie_description,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == movie_id
    assert response.json()["title"] == initial_movie_title
    assert response.json()["description"] == changed_movie_description


@pytest.mark.dependency(
    depends=[
        "test_create_movie",
        "test_get_one_movie",
        "test_patch_movie",
        "test_get_all_movies",
    ]
)
def test_delete_movie(request):
    movie_id = request.config.cache.get("movie_id", None)
    response = client.delete(f"/movies/delete/{movie_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["detail"] == "Movie Deleted"
