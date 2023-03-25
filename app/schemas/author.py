from typing import Optional
from pydantic import BaseModel


# Shared properties
class AuthorBase(BaseModel):
    name: Optional[str] = None


# Properties to receive via API
class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


# Properties shared by models stored in DB
class AuthorInDBBase(AuthorBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Author(AuthorInDBBase):
    pass
