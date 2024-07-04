# bookmanagement/models.py
from mongoengine import Document, StringField, DateField, FloatField

class Book(Document):
    title = StringField(max_length=200, required=True)
    author = StringField(max_length=100, required=True)
    published_date = DateField(required=True)
    genre = StringField(max_length=50, required=True)
    price = FloatField(required=True)

    def __str__(self):
        return self.title
