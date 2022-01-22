from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class Movie(BaseModel):
    id: Optional[UUID]
    title: str
    description: str

    class Config:
        orm_mode = True


class DeleteMovieResponse(BaseModel):
    detail: str


class UpdateMovie(BaseModel):
    id: UUID
    title: str
    description: str

    class Config:
        orm_mode = True
