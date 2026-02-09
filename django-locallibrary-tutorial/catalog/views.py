from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    #expansion 5.2
    word_to_search = "a"

    num_books_contain = Book.objects.filter(
        title__icontains=word_to_search
    ).count()

    num_genre_contain = Genre.objects.filter(
        name__icontains=word_to_search
    ).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': Genre.objects.count(),
        'word_to_search': word_to_search,
        'num_books_contain': num_books_contain,
        'num_genre_contain': num_genre_contain,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2    

class AuthorDetailView(generic.DetailView):
    model = Author