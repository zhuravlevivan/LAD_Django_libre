from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('authors/', views.authors, name='authors'),  # default
    re_path(r'^authors/(?P<a>\w+)/', views.authors),
    path('books/', views.books, name='books'),  # default
    # path('book/<int:book_id>/', views.show_book, name='book'),
    path('book/<slug:book_slug>/', views.show_book, name='book'),
    path('about/', views.about, name='about'),  # default
    path('add_note/', views.add_note, name='add_note'),  # default
    path('help/', views.help_page, name='help'),  # default
    path('sign/', views.sign_in, name='sign'),  # default

]
