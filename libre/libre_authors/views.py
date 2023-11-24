from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
def index(request):
    return HttpResponse("Page Libre_authors app")


def authors(request, authors='Not Set'):  # http://127.0.0.1:8000/authors/?a=Shultz&book=Python
    a = request.GET.get('a', authors)
    book = request.GET.get('book', 'No Book')
    output = '<h3>Author Name: {0}<br>Book: {1}</h3>'.format(a, book)
    return HttpResponse(output)

