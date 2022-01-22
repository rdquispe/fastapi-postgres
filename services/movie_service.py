from uuid import UUID

from sqlalchemy.orm import Session
from database.models import Movies
from schemas.models import DeleteMovieResponse, Movie, UpdateMovie


def movie_create(db: Session, movie: Movie):
    db_movie = Movies(title=movie.title, description=movie.description)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def movies_get_all(db: Session):
    return db.query(Movies).all()


def movie_get_one(db: Session, id: UUID):
    return db.query(Movies).filter_by(id=id).one()


def movie_update(db: Session, movie: UpdateMovie):
    update_query = {Movies.title: movie.title, Movies.description: movie.description}
    db.query(Movies).filter_by(id=movie.id).update(update_query)
    db.commit()
    return db.query(Movies).filter_by(id=movie.id).one()


def movie_delete(db: Session, id: UUID):
    movie = db.query(Movies).filter_by(id=id).all()
    if not movie:
        return DeleteMovieResponse(detail="Doesnt Exist")
    db.query(Movies).filter_by(id=id).delete()
    db.commit()
    return DeleteMovieResponse(detail="Movie Deleted")
