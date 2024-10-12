from typing import Optional
from pydantic import BaseModel


class CreateBook(BaseModel):
    title: str
    author: str


class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    is_borrowed: bool


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
