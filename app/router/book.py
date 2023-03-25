from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models import BookModel
from app.schemas import Book, BookCreate, BookUpdate

book_router = APIRouter(prefix="/book", tags=["book"])


@book_router.get("/", response_model=List[Book])
def get_book(
        db: Session = Depends(get_db),
) -> Any:
    book = db.query(BookModel).all()
    return book


@book_router.get("/{book_id}", response_model=Book)
def get_book_by_id(
        id: int,
        db: Session = Depends(get_db)
) -> Any:
    book = db.query(BookModel).filter(BookModel.id == id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Item not found")

    return book


@book_router.post("/", response_model=Book)
def create_book(
        book_in: BookCreate,
        db: Session = Depends(get_db),
) -> Any:
    book = BookModel(**book_in.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@book_router.put("/{book_id}", response_model=Book)
def update_book(
        id: int,
        book_in: BookUpdate,
        db: Session = Depends(get_db)
) -> Any:
    book = db.query(BookModel).get(id)

    if not book:
        raise HTTPException(status_code=404, detail="Item not found")

    book.title = book_in.title
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@book_router.delete("/", response_model=Book)
def delete_book(id: int, db: Session = Depends(get_db)) -> Any:
    book = db.query(BookModel).get(id)

    if not book:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(book)
    db.commit()
    return book
