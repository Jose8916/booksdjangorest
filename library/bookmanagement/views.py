# bookmanagement/views.py
from rest_framework import generics
from rest_framework_mongoengine.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.response import Response

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.all().order_by('id')  # Forzar recarga y ordenación

class BookCreate(generics.CreateAPIView):
    serializer_class = BookSerializer

class BookRetrieve(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs.get(self.lookup_field))
        return obj

class BookUpdate(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs.get(self.lookup_field))
        return obj

class BookDelete(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs.get(self.lookup_field))
        return obj

class BookPriceAverage(APIView):
    def get(self, request, year, format=None):
        pipeline = [
            {
                "$match": {
                    "published_date": {
                        "$gte": datetime(year, 1, 1),
                        "$lt": datetime(year + 1, 1, 1)
                    }
                }
            },
            {
                "$group": {
                    "_id": None,
                    "averagePrice": {"$avg": "$price"}
                }
            }
        ]
        result = Book.objects.aggregate(pipeline)
        average_price = 0
        for data in result:
            average_price = data.get('averagePrice', 0)
        
        return Response({"year": year, "average_price": average_price})