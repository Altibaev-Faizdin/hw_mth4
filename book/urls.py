from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list_view, name='book_list'),
    path('books/<int:id>/', views.book_detail_view, name='book_detail'),

    path('books/create/', views.create_book_view, name='create_book'),
    path('books/<int:id>/update/', views.update_book_view, name='update_book'),
    path('books/<int:id>/delete/', views.delete_book_view, name='delete_book'),
]
