from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250, unique=True)
    publisher = models.CharField(max_length=250)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

