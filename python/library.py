# library_manager/book.py
class Book:
    def __init__(self, title: str, author: str, isbn: str, status: str = "available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "status": self.status}

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"], d["author"], d["isbn"], d.get("status", "available"))

    def is_available(self):
        return self.status == "available"

    def issue(self):
        if not self.is_available():
            raise ValueError(f"Book '{self.title}' is already issued.")
        self.status = "issued"

    def return_book(self):
        if self.is_available():
            raise ValueError(f"Book '{self.title}' is not issued.")
        self.status = "available"
# library_manager/inventory.py
import json
from pathlib import Path
import logging
from book import Book

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, filepath="data/books.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load()

    def load(self):
        try:
            if not self.filepath.exists():
                self.filepath.parent.mkdir(parents=True, exist_ok=True)
                self.save()  # create empty file
            with self.filepath.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book.from_dict(d) for d in data]
            logger.info("Loaded books from %s", self.filepath)
        except json.JSONDecodeError:
            logger.error("JSON decode error: starting with empty catalog")
            self.books = []
        except Exception as e:
            logger.error("Error loading books: %s", e)
            self.books = []

    def save(self):
        try:
            with self.filepath.open("w", encoding="utf-8") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=2)
            logger.info("Saved books to %s", self.filepath)
        except Exception as e:
            logger.error("Error saving books: %s", e)
            raise

    def add_book(self, book: Book):
        if self.search_by_isbn(book.isbn):
            raise ValueError("ISBN already exists.")
        self.books.append(book)
        self.save()

    def search_by_title(self, title_substr: str):
        s = title_substr.lower()
        return [b for b in self.books if s in b.title.lower()]

    def search_by_isbn(self, isbn: str):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return list(self.books)

    def issue_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found.")
        book.issue()
        self.save()

    def return_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found.")
        book.return_book()
        self.save()
# cli/main.py
import logging
from library_manager.inventory import LibraryInventory
from library_managerbook import Book

def main():
    logging.basicConfig(filename='library.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')
    inv = LibraryInventory()
    while True:
        print("\nLibrary Inventory Manager")
        print("1) Add Book\n2) Issue Book\n3) Return Book\n4) View All Books\n5) Search Book\n6) Exit")
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                isbn = input("ISBN: ").strip()
                book = Book(title, author, isbn)
                inv.add_book(book)
                print("Book added.")
            elif choice == "2":
                isbn = input("ISBN to issue: ").strip()
                inv.issue_book(isbn)
                print("Book issued.")
            elif choice == "3":
                isbn = input("ISBN to return: ").strip()
                inv.return_book(isbn)
                print("Book returned.")
            elif choice == "4":
                for b in inv.display_all():
                    print(b)
            elif choice == "5":
                t = input("Search by (1) Title or (2) ISBN? ")
                if t == "1":
                    q = input("Title substring: ").strip()
                    results = inv.search_by_title(q)
                    if results:
                        for r in results: print(r)
                    else: print("No results.")
                else:
                    q = input("ISBN: ").strip()
                    b = inv.search_by_isbn(q)
                    print(b if b else "Not found.")
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            logging.error("Operation failed: %s", e)
            print("Error:", e)

if __name__ == "__main__":
    main()
