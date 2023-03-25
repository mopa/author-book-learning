from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import Author, AuthorCreate, AuthorUpdate
from app.models import AuthorModel, BookModel
from app.database.connection import get_db

author_router = APIRouter(prefix="/author", tags=["author"])


@author_router.get("/", response_model=List[Author])
def get_author(
        db: Session = Depends(get_db),
) -> Any:
    authors = db.query(AuthorModel).all()
    return authors


@author_router.get("/{author_id}", response_model=Author)
def get_author_by_id(
        author_id: int,
        db: Session = Depends(get_db),
) -> Any:
    author = db.query(AuthorModel).filter(AuthorModel.id == author_id).first()

    if not author:
        raise HTTPException(status_code=404, detail="Item not found")

    return author


@author_router.post("/", response_model=Author)
def create_author(
        author_in: AuthorCreate,
        db: Session = Depends(get_db),
) -> Any:
    author = AuthorModel(**author_in.dict())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@author_router.put("/{author_id}", response_model=Author)
def update_author(
        author_id: int,
        author_in: AuthorUpdate,
        db: Session = Depends(get_db),
):
    author = db.query(AuthorModel).filter(AuthorModel.id == author_id).first()

    if not author:
        raise HTTPException(status_code=404, detail="Item not found")

    author.name = author_in.name
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@author_router.delete("/", response_model=Author)
def delete_author(
        author_id: int,
        db: Session = Depends(get_db),
):
    author = db.query(AuthorModel).get(author_id)

    if not author:
        raise HTTPException(status_code=404, detail="Item not found")

    book_author_id = db.query(BookModel).filter(BookModel.author_id == author_id).first()

    if book_author_id:
        raise HTTPException(status_code=400, detail="Author has books")

    db.delete(author)
    db.commit()
    return author
