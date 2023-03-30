from typing import List, Any

from fastapi import APIRouter

from app.application.author_use_case import AuthorUseCase
from app.schemas import Author, AuthorCreate, AuthorUpdate

author_router = APIRouter(prefix="/author", tags=["author"])


@author_router.get("/", response_model=List[Author])
def get_author() -> Any:
    authors = AuthorUseCase().get_all()
    return authors


@author_router.get("/{author_id}", response_model=Author)
def get_author_by_id(author_id: int) -> Any:
    author = AuthorUseCase().get_by_id(author_id)
    return author


@author_router.post("/", response_model=Author)
def create_author(author_in: AuthorCreate) -> Any:
    author = AuthorUseCase().add(author_in)
    return author


@author_router.put("/{author_id}", response_model=Author)
def update_author(
        author_id: int,
        author_in: AuthorUpdate,
) -> Any:
    author = AuthorUseCase().update(author_in, author_id)
    return author


@author_router.delete("/", response_model=Author)
def delete_author(author_id: int) -> Any:
    author = AuthorUseCase().delete(author_id)
    return author
