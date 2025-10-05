class Book:
    """Represents a book with a title, author, and availability state."""
    def __init__(self, title, author):
        self.title = title               # public attribute
        self.author = author             # public attribute
        self._is_checked_out = False     # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out. Return True on success, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned/available. Return True on success, False if it was not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Simple library that manages a private list of Book instances."""
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out the first book that matches the title.
        Returns True if checkout succeeded, False otherwise (not found or already checked out).
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Return the first book that matches the title.
        Returns True if return succeeded, False otherwise (not found or already available).
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """Print all available books (title by author), one per line."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
