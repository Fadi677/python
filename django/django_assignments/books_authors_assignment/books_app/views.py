from django.shortcuts import render, redirect
from books_app import models

def index(request):
    context={
        'list_of_books' : models.all_books()
    }
    return render(request,'main.html',context)

def addbook(request):
    models.add_new_book(request.POST['title'],request.POST['desc'])
    return redirect('/')

def authors(request):
    context={
        'list_of_authors' : models.all_authors()
    }
    return render(request,'addauthor.html',context)

def addauthor(request):
    models.add_new_author(request.POST['firstname'],request.POST['lastname'],request.POST['notes'])
    return redirect('/authors')

def reshowbook(request,bookid):
    models.getbook(bookid)
    return redirect('books/<int:bookid>')

def showbook(request,bookid):
    context={
        'this_book' : models.getbook(bookid),
    }
    return render(request,'mybook.html',context)

def reshowauthor(request,authorid):
    models.getauthor(authorid)
    return redirect('authors/<int:bookid>')

def showauthor(request,authorid):
    context={
        'this_author' : models.getauthor(authorid),
    }
    return render(request,'myauthor.html',context)