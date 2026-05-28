#Library Management System


from datetime import datetime, timedelta
import json

class BookNotAvailableError(Exception):
    """Exception raised when a user tries to borrow an unavailable book."""
    pass


class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.due_date = None

    def __str__(self):
        status = f"Borrowed (Due: {self.due_date})" if self.is_borrowed else "Available"
        return f"[{self.book_id}] '{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = {}  

    def add_book(self, book: Book):
        """Adds a new book to the library catalog."""
        self.books[book.book_id] = book

    def borrow_book(self, book_id: str, user: str):
        """Lends a book and sets a 14-day due date."""
        book = self.books.get(book_id)
        
        if not book:
            print(f"Error: Book ID {book_id} not found.")
            return

        if book.is_borrowed:
            raise BookNotAvailableError(f"Sorry, '{book.title}' is already checked out.")

        book.is_borrowed = True
        book.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        
        self._log_transaction(user, book_id, "BORROW")
        print(f"Success! {user} borrowed '{book.title}'. Due date: {book.due_date}")

    def return_book(self, book_id: str, user: str):
        """Returns a borrowed book."""
        book = self.books.get(book_id)
        
        if book and book.is_borrowed:
            book.is_borrowed = False
            book.due_date = None
            self._log_transaction(user, book_id, "RETURN")
            print(f"Success! '{book.title}' has been returned.")
        else:
            print(f" Error: Book ID {book_id} was not borrowed.")

    def _log_transaction(self, user: str, book_id: str, action: str):
        """Appends the transaction details to a JSON log file."""
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user,
            "book_id": book_id,
            "action": action
        }
        
        try:
            with open("library_logs.txt", "a") as file:
                file.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            print(f"Failed to write to log file: {e}")

    def get_available_books(self):
        """Returns a list of all currently available books."""
        return [book for book in self.books.values() if not book.is_borrowed]


if __name__ == "__main__":
    my_library = Library()
    my_library.add_book(Book("B101", "The Hobbit", "J.R.R. Tolkien"))
    my_library.add_book(Book("B102", "1984", "George Orwell"))
    my_library.add_book(Book("B103", "Dune", "Frank Herbert"))

    print("--- Current Inventory ---")
    for b in my_library.books.values():
        print(b)

    print("\n--- Processing Transactions ---")
    my_library.borrow_book("B102", "Alice")

    try:
        my_library.borrow_book("B102", "Bob")
    except BookNotAvailableError as e:
        print(e)

    # Return the book
    print("\n--- Processing Returns ---")
    my_library.return_book("B102", "Alice")

    print("\n--- Available Books Now ---")
    available = my_library.get_available_books()
    for b in available:
        print(b)