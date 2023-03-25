from typing import Optional
from pydantic import BaseModel


# Shared properties
class BookBase(BaseModel):
    name: Optional[str] = None


# Properties to receive via API
class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


# Properties shared by models stored in DB
class BookInDBBase(BookBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Book(BookInDBBase):
    pass
