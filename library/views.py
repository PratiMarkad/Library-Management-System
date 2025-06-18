from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, Book
from .models import Book
from django.contrib.auth.models import User
from django.db import models
from .models import Student



def admin_signup(request):
    if request.method == 'POST':
        if Admin.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email already exists')
        else:
            Admin.objects.create(
                name=request.POST['name'],
                # email=request.POST['email'],
                email = request.POST.get('email'),
                password=request.POST['password']
            )
            messages.success(request, 'Account created!')
            return redirect('admin_login')
    return render(request, 'library/admin_signup.html')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        email = request.POST.get('email')
        password = request.POST['password']
        if Admin.objects.filter(email=email, password=password).exists():
            request.session['admin'] = email
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'library/admin_login.html')

def dashboard(request):
    if 'admin' not in request.session:
        return redirect('admin_login')
    books = Book.objects.all()
    return render(request, 'library/dashboard.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            # isbn=request.POST['isbn'],
            isbn=request.POST['isbn'].replace('-', ''),
            publisher=request.POST['publisher'],
            year=request.POST['year']
        )
        return redirect('dashboard')
    return render(request, 'library/add_book.html')

def update_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.publisher = request.POST['publisher']
        book.year = request.POST['year']
        book.save()
        return redirect('dashboard')
    return render(request, 'library/update_book.html', {'book': book})


def update_book(request, id):  
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.publisher = request.POST['publisher']
        book.year = request.POST['year']
        book.save()
        return redirect('dashboard')
    return render(request, 'library/update_book.html', {'book': book})



def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return redirect('dashboard')

def all_books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'library/all_books.html', {'books': books})

def student_view(request):
    books = Book.objects.all()
    return render(request, 'library/student_view.html', {'books': books})


def student_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # optional

    books = Book.objects.all()
    return render(request, 'library/student_dashboard.html', {'books': books})

def login_redirect(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    elif hasattr(request.user, 'student'):
        return redirect('student_dashboard')
    else:
        return redirect('dashboard')

def all_books(request):
    books = Book.objects.all()  
    return render(request, 'library/book_list.html', {'books': books})

# class Student(models.Model):
class Student:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.user.username
    
