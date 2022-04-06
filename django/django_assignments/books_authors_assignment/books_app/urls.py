from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),#main books page
    path('addbook',views.addbook),#add book method
    path('authors',views.authors),##main authors page
    path('addauthor',views.addauthor),#add author method
    path('books/<int:bookid>',views.showbook),#displays certain book
    path('authors/<int:authorid>',views.showauthor),#displays certain author
    path('addtobook',views.add_author_book),#adds an author to a book
    path('addtoauthor',views.add_book_author)#adds a book to an author
]