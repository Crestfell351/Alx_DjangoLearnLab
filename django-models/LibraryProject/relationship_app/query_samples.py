from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name='George Orwell')
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(f"Title: {book.title}, Author: {book.author.name}")

# List all books in a library
library = Library.objects.get(name='Central Library')
books_in_library = library.books.all()
for book in books_in_library:
    print(f"Library: {library.name}, Book: {book.title}")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian: {librarian.name}, Library: {librarian.library.name}")
