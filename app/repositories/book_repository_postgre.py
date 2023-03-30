from app.schemas import Book
from .i_book_repository import IBookRepository


class BookRepositoryPostgre(IBookRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(Book).all()

    def get_by_id(self, id):
        return self.db.query(Book).filter(Book.id == id).first()

    def add(self, book):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)

    def update(self, book):
        self.db.commit()
        self.db.refresh(book)

    def delete(self, id):
        book = self.db.query(Book).filter(Book.id == id).first()
        self.db.delete(book)
        self.db.commit()