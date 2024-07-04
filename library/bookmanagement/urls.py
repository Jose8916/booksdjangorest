# bookmanagement/urls.py
from django.urls import path
from .views import BookList, BookCreate, BookRetrieve, BookUpdate, BookDelete, BookPriceAverage

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/create/', BookCreate.as_view(), name='book-create'),
    path('books/<str:id>/', BookRetrieve.as_view(), name='book-retrieve'),
    path('books/<str:id>/update/', BookUpdate.as_view(), name='book-update'),
    path('books/<str:id>/delete/', BookDelete.as_view(), name='book-delete'),
    path('books/average_price/<int:year>/', BookPriceAverage.as_view(), name='book-average-price'),
]
