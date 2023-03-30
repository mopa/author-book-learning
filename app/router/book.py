from typing import List, Any

from fastapi import APIRouter

from app.application.book_use_case import BookUseCase
from app.schemas import Book, BookCreate, BookUpdate, BookAll

book_router = APIRouter(prefix="/book", tags=["book"])


@book_router.get("/", response_model=List[BookAll])
def get_book() -> Any:
    book = BookUseCase().get_all()
    return book


@book_router.get("/{book_id}", response_model=Book)
def get_book_by_id(id: int) -> Any:
    book = BookUseCase().get_by_id(id)
    return book


@book_router.post("/", response_model=Book)
def create_book(book_in: BookCreate) -> Any:
    book = BookUseCase().add(book_in)
    return book


@book_router.put("/{book_id}", response_model=Book)
def update_book(
        id: int,
        book_in: BookUpdate,
) -> Any:
    book = BookUseCase().update(book_in, id)
    return book


@book_router.delete("/", response_model=Book)
def delete_book(id: int) -> Any:
    book = BookUseCase().delete(id)
    return book
