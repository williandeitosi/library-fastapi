from fastapi import APIRouter, HTTPException
from schemas.schema import CreateBook, BookResponse, BookUpdate
from models.Book import Book
from models.Library import Library
from typing import List

from handlers.create_book_handler import (
    create_book_handler,
    all_books_handler,
    get_book_handler,
    update_book_handler,
    borrow_book_handler,
    return_book_handler,
)

router = APIRouter()


@router.post("/books/", tags=["create"], response_model=BookResponse)
def create_book(book: CreateBook):
    return create_book_handler(book)


@router.get("/books/", tags=["list"], response_model=List[BookResponse])
def list_all_books():
    return all_books_handler()


@router.get("/books/{book_id}", tags=["read_book"], response_model=BookResponse)
def read_book(book_id: str):
    return get_book_handler(book_id)


@router.put("/books/{book_id}", tags=["update"], response_model=BookResponse)
def update_book(book_id: str, update_book: BookUpdate):
    return update_book_handler(book_id, update_book)


@router.put("/books/{book_id}/borrowed", tags=["borrow"])
def borrow_book(book_id: str):
    return borrow_book_handler(book_id)


@router.put("/books/{book_id}/return", tags=["return"])
def return_book(book_id: str):
    return return_book_handler(book_id)
