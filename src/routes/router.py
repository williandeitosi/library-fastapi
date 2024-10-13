from fastapi import APIRouter, HTTPException
from schemas.schema import CreateBook, BookResponse, BookUpdate
from models.Book import Book
from models.Library import Library
from typing import List

from handlers.create_book_handler import (
    create_book_handler,
    all_books_handler,
    get_book_handler,
)

router = APIRouter()

library = Library()


@router.post("/books/", tags=["create"], response_model=BookResponse)
def create_book(book: CreateBook):
    return create_book_handler(book)


@router.get("/books/", tags=["list"], response_model=List[BookResponse])
def list_all_books():
    return all_books_handler()


@router.get("/books/{book_id}", tags=["read_book"], response_model=BookResponse)
def read_book(book_id: str):
    return get_book_handler(book_id)


# continuar criando os proximos handlers para melhorar a estrutura do codigo


@router.put("/books/{book_id}", tags=["update"], response_model=BookResponse)
def update_book(book_id, update_book: BookUpdate):
    try:
        book = library.get_book(book_id)
        if update_book.title is not None:
            book.title = update_book.title
        if update_book.author is not None:
            book.author = update_book.author
        return BookResponse(**book.__dict__)
    except ValueError:
        raise HTTPException(status_code=404, detail="Livro não encontrado")


@router.put("/books/{book_id}/borrowed", tags=["borrow"])
def borrow_book(book_id: str):
    try:
        book = library.get_book(book_id)
        book.borrow()
        return {"message": "Livro emprestado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/books/{book_id}/return", tags=["return"])
def return_book(book_id: str):
    try:
        book = library.get_book(book_id)
        book.return_book()
        return {"message": "Devolução do livro com sucesso!"}
    except ValueError as e:
        print(f"MEU ERRO: ", str(e))
        raise HTTPException(status_code=404, detail=str(e))
