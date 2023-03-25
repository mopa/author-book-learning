from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.models import AuthorModel
from app.database.connection import get_db

author_router = APIRouter(prefix="/author", tags=["author"])


@author_router.get("/", response_model=List[schemas.Author])
def get_author(
        db: Session = Depends(get_db),
):
    authors = db.query(AuthorModel).all()
    return authors


@author_router.get("/{author_id}", response_model=schemas.Author)
def get_author_by_id(author_id: int):
    return {"author_id": author_id}


@author_router.post("/")
def create_author():
    return {"author": "John Doe"}


@author_router.put("/{author_id}")
def update_author():
    return {"author": "John Doe"}


@author_router.delete("/")
def delete_author():
    return {"author": "John Doe"}
