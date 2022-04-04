from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes=models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def all_books():
    return Book.objects.all()

def add_new_book(new_title,new_desc):
    Book.objects.create(title=new_title,desc=new_desc)

def all_authors():
    return Author.objects.all()

def add_new_author(fname,lname,new_note):
    Author.objects.create(first_name=fname,last_name=lname,notes=new_note)

def getbook(bookid):
    return Book.objects.get(id=bookid)

def select_author(bookid,authorid):
    this_book=Book.objects.get(id=bookid)
    this_author=Author.objects.get(id=authorid)
    this_book.authors.add(this_author)

def getauthor(authorid):
    return Author.objects.get(id=authorid)

def select_book(bookid,authorid):
    this_book=Book.objects.get(id=bookid)
    this_author=Author.objects.get(id=authorid)
    this_author.books.add(this_author)