from django.shortcuts import render, redirect
from books_app import models

def books_page(request):
    context={
        'all_books' : models.all_books()
    }
    return render(request,'books.html',context)

def add_book(request):
    b_title=request.POST['title']
    b_desc=request.POST['desc']
    b_uploaded_by=request.session['id']
    print("--------",request.session['id'])
    models.create_book(b_title,b_desc,b_uploaded_by)
    return redirect('/books')

def add_to_fav(request):
    user_id=request.session['id']
    book_id=request.POST['book_id']
    models.add_book_to_fav(user_id,book_id)
    return redirect('/books')