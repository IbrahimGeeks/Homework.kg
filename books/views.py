from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Book


def book_list_view(request):
    books = Book.objects.all().order_by('id')
    

    search_query = request.GET.get('search_book')
    if search_query:
        books = books.filter(title__icontains=search_query)
        

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'books/book_list.html', {'page_obj': page_obj, 'search_query': search_query})


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    book.views_count += 1
    book.save()
    
    return render(request, 'books/book_detail.html', {'book': book})
