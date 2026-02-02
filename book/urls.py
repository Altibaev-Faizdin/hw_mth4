from django.urls import path
from . import views

urlpatterns = [
    path('anon/', views.book_list_view, name='book_list'),
    path('anon/<int:id>/', views.book_detail_view, name='book_detail'), 
]   
