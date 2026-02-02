from django.shortcuts import render, get_object_or_404
from . import models

def book_list_view(request):
    books = models.Book.objects.all()
    return render(
        request,
        'book_list.html', 
        {'books': books}
    )

def book_detail_view(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(
        request,
        'book_detail.html',
        {'book': book}
    )
