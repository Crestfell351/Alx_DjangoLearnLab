from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book, Author
from django.contrib.auth.models import User  
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create an author and some books for testing
        self.author = Author.objects.create(name='F. Scott Fitzgerald')
        self.book1 = Book.objects.create(title='The Great Gatsby', publication_year=1925, author=self.author)
        self.book2 = Book.objects.create(title='This Side of Paradise', publication_year=1920, author=self.author)
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()

    def test_create_book(self):
        """Test creating a new book."""
        url = reverse('book-create')
        data = {
            'title': 'Tender is the Night',
            'publication_year': 1934,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_books(self):
        """Test retrieving a list of books."""
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        """Test updating a book's details."""
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'The Great Gatsby (Updated)', 'publication_year': 1925, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Great Gatsby (Updated)')

    def test_delete_book(self):
        """Test deleting a book."""
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        url = reverse('book-list') + '?title=The Great Gatsby'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Great Gatsby')

    def test_search_books(self):
        """Test searching for books."""
        url = reverse('book-list') + '?search=Paradise'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'This Side of Paradise')

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication_year."""
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1920)  # Oldest book comes first
