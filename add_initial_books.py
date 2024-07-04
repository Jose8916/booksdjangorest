# bookmanagement/migrations/add_initial_books.py

from datetime import datetime
from mongoengine import connect
from bookmanagement.models import Book

# Conectar a la base de datos
connect(db='library_db', host='localhost', port=27017)

# Crear datos de prueba
books = [
    {
        "title": "Book One",
        "author": "Author One",
        "published_date": datetime(2020, 1, 1),
        "genre": "Fiction",
        "price": 15.99
    },
    {
        "title": "Book Two",
        "author": "Author Two",
        "published_date": datetime(2021, 2, 15),
        "genre": "Non-Fiction",
        "price": 12.49
    },
    {
        "title": "Book Three",
        "author": "Author Three",
        "published_date": datetime(2019, 3, 10),
        "genre": "Science Fiction",
        "price": 22.95
    },
    {
        "title": "Book Four",
        "author": "Author Four",
        "published_date": datetime(2022, 4, 5),
        "genre": "Fantasy",
        "price": 18.00
    },
    {
        "title": "Book Five",
        "author": "Author Five",
        "published_date": datetime(2018, 5, 25),
        "genre": "Mystery",
        "price": 9.99
    }
]

# Insertar datos en la base de datos
for book_data in books:
    book = Book(**book_data)
    book.save()

print("Datos de prueba insertados con éxito.")
