from django.urls import path
from . import views
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Retrieve a single book
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),  # Create a book
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
