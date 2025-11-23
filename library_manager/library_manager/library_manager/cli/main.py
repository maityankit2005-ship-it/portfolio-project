from library_manager.library_manager.cli.inventory import LibraryInventory
from  library_manager.library_manager.cli.library_manager.book import Book

def input_nonempty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty. Try again.")

def show_books(books):
    if not books:
        print(" (no books found)")
        return
    for i, b in enumerate(books, start=1):
        print(f"{i}. {b}")

def run_cli():
    inv = LibraryInventory()
    inv.load()  # load if json exists
    menu = """
Library Manager
1) Add Book
2) Issue Book (by ISBN)
3) Return Book (by ISBN)
4) View All Books
5) Search Book (title)
6) Search Book (ISBN)
7) Save Catalog
8) Exit
Enter choice (1-8): """

    while True:
        choice = input(menu).strip()
        if choice == "1":
            title = input_nonempty("Title: ")
            author = input_nonempty("Author: ")
            isbn = input_nonempty("ISBN (unique): ")
            ok = inv.add_book(Book(title, author, isbn))
            print("Added." if ok else "Duplicate ISBN. Not added.")

        elif choice == "2":
            isbn = input_nonempty("ISBN to issue: ")
            b = inv.search_by_isbn(isbn)
            if b and b.issue():
                print("Issued.")
            else:
                print("Issue failed (not found or already issued).")

        elif choice == "3":
            isbn = input_nonempty("ISBN to return: ")
            b = inv.search_by_isbn(isbn)
            if b and b.return_book():
                print("Returned.")
            else:
                print("Return failed (not found or not issued).")

        elif choice == "4":
            print("\nAll books:")
            show_books(inv.books)

        elif choice == "5":
            q = input_nonempty("Title search: ")
            show_books(inv.search_by_title(q))

        elif choice == "6":
            isbn = input_nonempty("ISBN: ")
            b = inv.search_by_isbn(isbn)
            print(b if b else "Not found.")

        elif choice == "7":
            print("Saving...", "Success." if inv.save() else "Save failed.")

        elif choice == "8":
            if input("Save before exit? (y/n): ").strip().lower() == "y":
                inv.save()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1-8.")

if __name__ == "__main__":
    run_cli()
