from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse

from .models import LibreAuthors

menu = [
    {'title': 'Books', 'url_name': 'books'},
    {'title': 'About', 'url_name': 'about'},
    # {'title': 'Add Note', 'url_name': 'add_note'},
    # {'title': 'Help', 'url_name': 'help'},
    {'title': 'Log In', 'url_name': 'login'},
]


def index(request):
    data = {'menu': menu, }
    return render(request, "libre_authors/index.html", context=data)


def authors(request, book_authors='Not Set'):  # http://127.0.0.1:8000/authors/?a=Shultz&book=Python
    a = request.GET.get('a', book_authors)
    book = request.GET.get('book', 'No Book')
    output = '<h3>Author Name: {0}<br>Book: {1}</h3>'.format(a, book)
    return HttpResponse(output)


def books(request):
    books_db = LibreAuthors.published.all()
    data = {'menu': menu, 'books': books_db, }
    return render(request, "libre_authors/books.html", context=data)


def show_book(request, book_slug):
    book = get_object_or_404(LibreAuthors, slug=book_slug)
    data = {
        'title': book.title,
        'menu': menu,
        'book': book,

    }
    return render(request, 'libre_authors/book.html', data)


def about(request):
    data = {'menu': menu, }
    return TemplateResponse(request, 'libre_authors/about.html', context=data)


def add_note(request):
    return HttpResponse('Add note page')


def help_page(request):
    return HttpResponse('Help page')


def login_user(request):
    data = {'menu': menu, }
    return TemplateResponse(request, 'libre_authors/login.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
