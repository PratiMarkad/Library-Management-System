# Library-Management-System
A Django-based Library Management System with MySQL integration that enables admin CRUD operations on books and allows students to view book records.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Create database:
CREATE DATABASE library_db;


 # Getting Started

1) Clone the repo:
git clone https://github.com/PratiMarkad/Library-Management-System.git
cd Library-Management-System

2) Create virtual environment:
python -m venv venv
venv\Scripts\activate

3) Install dependencies:
pip install -r requirements.txt

4) Run migrations:
python manage.py makemigrations
python manage.py migrate

5) Run the server:
python manage.py runserver

6) Visit:
http://127.0.0.1:8000/


##  Folder Structure

LibrarySystem/
├── library/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── library/
│           ├── base.html
│           ├── dashboard.html
│           ├── add_book.html
│           ├── update_book.html
│           ├── student_view.html
├── LibrarySystem/
│   └── settings.py
├── manage.py
├── requirements.txt
└── README.md

## Author
Pratibha Markad
