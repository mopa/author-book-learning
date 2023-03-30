from typing import Optional
from pydantic import BaseModel


# Shared properties
class BookBase(BaseModel):
    title: Optional[str] = None


# Properties to receive via API
class BookCreate(BookBase):
    author_id: int


class BookUpdate(BookBase):
    pass


# Properties shared by models stored in DB
class BookInDBBase(BookBase):
    id: int
    title: str

    class Config:
        orm_mode = True


# Properties to return to client
class Book(BookInDBBase):
    pass

class BookAll(BookInDBBase):
    author_id: int