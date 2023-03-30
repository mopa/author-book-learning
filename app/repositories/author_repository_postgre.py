from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import AuthorModel, BookModel
from .i_author_repository import IAuthorRepository
from app.database.connection import get_db


class AuthorRepositoryPostgre(IAuthorRepository):
    def __init__(self):
        self.db: Session = get_db().__next__()

    def get_all(self):
        return self.db.query(AuthorModel).all()

    def get_by_id(self, id):
        author = self.db.query(AuthorModel).filter(AuthorModel.id == id).first()

        if not author:
            raise HTTPException(status_code=404, detail="Item not found")

        return author

    def add(self, author_in):
        author = AuthorModel(**author_in.dict())
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)
        return author

    def update(self, author_in, id):
        author = self.db.query(AuthorModel).filter(AuthorModel.id == id).first()

        if not author:
            raise HTTPException(status_code=404, detail="Item not found")

        author.name = author_in.name
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)
        return author

    def delete(self, id):
        author = self.db.query(AuthorModel).get(id)

        if not author:
            raise HTTPException(status_code=404, detail="Item not found")

        book_author_id = self.db.query(BookModel).filter(BookModel.author_id == id).first()

        if book_author_id:
            raise HTTPException(status_code=400, detail="Author has books")

        self.db.delete(author)
        self.db.commit()
        return author
