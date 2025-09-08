#!/usr/bin/env python

import sys
import logging
from typing import Iterable
from . import DefaultLibrary, LibraryManager, Book


def main():
    library = DefaultLibrary(log_info_book_printer)
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        try:
            match command:
                case "add":
                    title = input("Enter book title: ").strip()
                    author = input("Enter book author: ").strip()
                    year = input("Enter book year: ").strip()
                    if (title or author or year) == "":
                        raise ValueError("All fields are required.")
                    manager.add_book(title, author, int(year))
                case "remove":
                    title = input("Enter book title to remove: ").strip()
                    if title == "":
                        raise ValueError("Title is required.")
                    manager.remove_book(title)
                case "show":
                    manager.show_books()
                case "exit":
                    break
                case _:
                    print("Invalid command. Please try again.")
        except ValueError as ex:
            print(f"Error: {ex}", file=sys.stderr)


def log_info_book_printer(books: Iterable[Book]):
    for book in books:
        logging.info(
            "Title: %s, Author: %s, Year: %d", book.title, book.author, book.year
        )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
