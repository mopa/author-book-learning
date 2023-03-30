from fastapi import HTTPException
from sqlalchemy.orm import Session

from .i_book_repository import IBookRepository
from app.database.connection import get_db
from app.models import BookModel


class BookRepositoryPostgre(IBookRepository):
    def __init__(self):
        self.db: Session = get_db().__next__()

    def get_all(self):
        return self.db.query(BookModel).all()

    def get_by_id(self, id):
        book = self.db.query(BookModel).filter(BookModel.id == id).first()

        if not book:
            raise HTTPException(status_code=404, detail="Item not found")

        return book

    def add(self, book_in):
        book = BookModel(**book_in.dict())
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, book_in, id):
        book = self.db.query(BookModel).get(id)

        if not book:
            raise HTTPException(status_code=404, detail="Item not found")

        book.title = book_in.title
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def delete(self, id):
        book = self.db.query(BookModel).get(id)

        if not book:
            raise HTTPException(status_code=404, detail="Item not found")

        self.db.delete(book)
        self.db.commit()
        return book
