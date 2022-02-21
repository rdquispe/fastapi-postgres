from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.models import DeleteMovieResponse, Movie, UpdateMovie
from services.movies import (
    movie_create,
    movie_delete,
    movie_get_one,
    movie_update,
    movies_get_all,
)

movies_router = APIRouter(tags=["movies"])


@movies_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Movie)
def create_movie(movie: Movie, db: Session = Depends(get_db)):
    return movie_create(db=db, movie=movie)


@movies_router.get("/list/all", status_code=status.HTTP_200_OK, response_model=List[Movie])
def get_all_movies(db: Session = Depends(get_db)):
    return movies_get_all(db=db)


@movies_router.get("/get/{id}", status_code=status.HTTP_200_OK, response_model=Movie)
def get_one_movie(id, db: Session = Depends(get_db)):
    return movie_get_one(db=db, id=id)


@movies_router.delete("/delete/{id}", status_code=status.HTTP_200_OK, response_model=DeleteMovieResponse)
def delete_movie(id, db: Session = Depends(get_db)):
    delete_status = movie_delete(db=db, id=id)
    if delete_status.detail == "Doesnt Exist":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found")
    else:
        return delete_status


@movies_router.patch("/update", status_code=status.HTTP_200_OK, response_model=Movie)
def update_movie(movie: UpdateMovie, db: Session = Depends(get_db)):
    return movie_update(db=db, movie=movie)
