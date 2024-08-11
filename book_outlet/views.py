from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg
# Create your views here.

def starting_page(request):
    books = Book.objects.all().order_by('-rating')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/starting-page.html', {
        'books': books,
        'total_number_of_books': num_books,
        'avg_rating' : avg_rating
    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book-detail.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_best_selling": book.is_best_selling
    })