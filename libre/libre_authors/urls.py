from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('authors/', views.authors),  # default
    re_path(r'^authors/(?P<a>\w+)/', views.authors),


]