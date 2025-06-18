from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('signup/', views.admin_signup, name='admin_signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-book/', views.add_book, name='add_book'),
    path('update-book/<int:id>/', views.update_book, name='update_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),
    path('all-books/', views.all_books, name='all_books'),
    path('student/', views.student_view, name='student_view'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('redirect/', views.login_redirect, name='login_redirect'),
    path('all-books/', views.all_books, name='all_books'),
]
