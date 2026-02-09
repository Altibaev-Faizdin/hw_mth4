from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms


def book_list_view(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail_view(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book': book})


def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = forms.BookForm()

    return render(request, 'create_book.html', {'form': form})


def update_book_view(request, id):
    book = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(
            request.POST,
            request.FILES,
            instance=book
        )
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = forms.BookForm(instance=book)

    return render(request, 'update_book.html', {'form': form})


def delete_book_view(request, id):
    book = get_object_or_404(models.Book, id=id)
    book.delete()
    return redirect('/books/')
