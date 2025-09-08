from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Protocol


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        raise NotImplementedError

    @abstractmethod
    def remove_book(self, title: str):
        raise NotImplementedError

    @abstractmethod
    def show_books(self):
        raise NotImplementedError


class BooksPrinter(Protocol):
    def __call__(self, books: Iterable[Book]): ...


def default_book_printer(books: Iterable[Book]):
    for book in books:
        print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")


class DefaultLibrary(LibraryInterface):
    def __init__(self, books_printer: BooksPrinter = default_book_printer):
        self.books = []
        self.books_printer = books_printer

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def show_books(self):
        self.books_printer(self.books)


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()
