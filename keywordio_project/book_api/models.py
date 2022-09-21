from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=16)
    author_name = models.CharField(max_length=16)
    publisher = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    reviews = models.CharField(max_length=50)