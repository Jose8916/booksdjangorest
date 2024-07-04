# bookmanagement/tests.py
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from datetime import datetime

class BookTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "published_date": datetime(2021, 1, 1),
            "genre": "Test Genre",
            "price": 19.99
        }
        cls.book = Book.objects.create(**cls.book_data)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['results']), 0)  # Assuming pagination is enabled

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_date": "2023-07-05",
            "genre": "New Genre",
            "price": 29.99
        }
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")
