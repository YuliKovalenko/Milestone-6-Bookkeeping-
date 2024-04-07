'''classDiagram
class Book {
  - title: String
  - author: String
  - category: String
}

class Shelf {
  - name: String
  - +books: Set<Book>

  + add_book(book: Book): void
  + remove_book(book: Book): void
}

class Room {
  - +shelves: List<Shelf>

  + add_shelf(shelf: Shelf): void
  + remove_shelf(shelf: Shelf): void
  + organize_books_by_category(books: List[Book]): void
  + sort_books_by_title(): void
}'''

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"{self.title} by {self.author} ({self.category})"


class Shelf:
    def __init__(self, name):
        self.name = name
        self.books = set()  # Using a set to ensure uniqueness of books

    def add_book(self, book):
        self.books.add(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def __str__(self):
        return f"{self.name} Shelf: {', '.join(map(str, self.books))}"


class Room:
    def __init__(self):
        self.shelves = []

    def add_shelf(self, shelf):
        self.shelves.append(shelf)

    def remove_shelf(self, shelf):
        if shelf in self.shelves:
            self.shelves.remove(shelf)

    def organize_books_by_category(self, books):
    # Create a dictionary to store books by category
        books_by_category = {}
        for book in books:
            books_by_category.setdefault(book.category, []).append(book)

    # Clear existing books from shelves
        for shelf in self.shelves:
            shelf.books.clear()

    # Add books to shelves based on category
        for category, books in books_by_category.items():
            for book in books:
        # Find or create a shelf for the category
                shelf = next((s for s in self.shelves if s.name == category), Shelf(category))
                self.add_shelf(shelf)
                shelf.add_book(book)

    def sort_books_by_title(self):
        for shelf in self.shelves:
      # Sort books on the shelf by title
            shelf.books = sorted(shelf.books, key=lambda b: b.title)

    def __str__(self):
        return "\n".join(map(str, self.shelves))


# Example usage
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy")
book2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Sci-Fi")
book3 = Book("The Alchemist", "Paulo Coelho", "Self-Help")

shelf1 = Shelf("Fiction")
shelf2 = Shelf("Non-Fiction")

room = Room()

room.add_shelf(shelf1)
room.add_shelf(shelf2)

room.organize_books_by_category([book1, book2, book3])

print(room)