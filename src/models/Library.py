from models import Book


class Library:
    def __init__(self):
        self.list_books = {}

    def add_book(self, book: Book):
        self.list_books[book.id] = book

    def remove_book(self, book_id: str):
        if book_id not in self.list_books:
            raise ValueError("Livro nao encontrado")
        del self.list_books[book_id]

    def get_book(self, book_id: str):
        if book_id not in self.list_books:
            raise ValueError("Livro nao encontrado")
        return self.list_books[book_id]

    def get_all_books(self):
        return list(self.list_books.values())
