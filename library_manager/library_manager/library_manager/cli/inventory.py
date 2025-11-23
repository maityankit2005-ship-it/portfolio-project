import json
import os
from library_manager.library_manager.cli.library_manager.book import Book

CATALOG_FILE = os.path.join(os.path.dirname(__file__), "library_catalog.json")

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> bool:
        if any(b.isbn == book.isbn for b in self.books):
            return False
        self.books.append(book)
        return True

    def search_by_isbn(self, isbn: str):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def search_by_title(self, query: str):
        q = query.lower()
        return [b for b in self.books if q in b.title.lower()]

    def display_all(self):
        return [str(b) for b in self.books]

    def save(self, path: str = CATALOG_FILE) -> bool:
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=2)
            return True
        except Exception:
            return False

    def load(self, path: str = CATALOG_FILE) -> bool:
        if not os.path.exists(path):
            return False
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [Book(**item) for item in data]
            return True
        except Exception:
            return False
