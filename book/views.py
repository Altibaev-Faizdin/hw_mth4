from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Book
from .forms import BookForm
from django.views import generic
from django.urls import reverse_lazy



class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'page_obj'
    model = Book
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        books = Book.objects.all()
        if query:
            books = books.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query)
            )
        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book'
    model = Book
    pk_url_kwarg = 'id'


class BookCreateView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = BookForm
    model = Book
    success_url = reverse_lazy('book_list')


class BookUpdateView(generic.UpdateView):
    template_name = 'update_book.html'
    form_class = BookForm
    model = Book
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')


class BookDeleteView(generic.DeleteView):
    model = Book
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)














# def book_list_view(request):
#     query = request.GET.get('q')
#     books = Book.objects.all()

#     if query:
#         books = books.filter(
#             Q(title__icontains=query) |
#             Q(author__icontains=query)
#         )

#     paginator = Paginator(books, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'book_list.html', {
#         'page_obj': page_obj,
#         'query': query
#     })


# def book_detail_view(request, id):
#     book = get_object_or_404(Book, id=id)
#     return render(request, 'book_detail.html', {'book': book})


# def create_book_view(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()

#     return render(request, 'create_book.html', {'form': form})


# def update_book_view(request, id):
#     book = get_object_or_404(Book, id=id)

#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm(instance=book)

#     return render(request, 'update_book.html', {'form': form})


# def delete_book_view(request, id):
#     book = get_object_or_404(Book, id=id)
#     book.delete()
#     return redirect('book_list')
