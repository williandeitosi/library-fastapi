from fastapi import HTTPException
from schemas.schema import CreateBook, BookResponse
from models.Book import Book
from models.Library import Library

library = Library()


def create_book_handler(book: CreateBook) -> BookResponse:
    new_book = Book(title=book.title, author=book.author)
    res = library.add_book(new_book)
    print(res)
    return BookResponse(**new_book.__dict__)


def all_books_handler():
    return [BookResponse(**book.__dict__) for book in library.get_all_books()]


def get_book_handler(book_id: str):
    try:
        book = library.get_book(book_id)
        return BookResponse(**book.__dict__)
    except ValueError:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
