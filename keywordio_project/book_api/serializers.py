# from dataclasses import field
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book
        field = '__all__'