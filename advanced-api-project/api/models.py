from django.db import models

class Author(models.Model):
    # Author represents a person who writes books.
    # One author can have many books (one-to-many relationship).
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Book represents a book written by an author.
    # Each book is linked to an author using a ForeignKey relationship.
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
