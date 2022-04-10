from django.db import models
from users_app.models import *

class BookManager(models.Manager):
    def add_book_validator(self,postData):
        errors={}
        if len(postData['title']<1):
            errors['title']="Please Enter a Title For The Book"
        if len(postData['desc'])<5:
            errors['desc']="Please Enter a Valid Description Of The Book"
        return errors

class Book(models.Model):
    title=models.CharField(max_length=255, null=False)
    desc=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    uploaded_by=models.ForeignKey(User, related_name="uploaded_books",on_delete=models.CASCADE) #user_id
    liked_by=models.ManyToManyField(User, related_name="liked_books")
    objects=BookManager()


def all_books():
    return Book.objects.all()

def add_book_to_fav(user_id,book_id):
    user_f=User.objects.get(id=user_id)
    book_f=Book.objects.get(id=book_id)
    user_f.uploaded_books.add(book_f)

def create_book(title,description,uploader_id):
    uploader= User.objects.get(id=uploader_id)
    this_book=Book.objects.create(title=title, desc=description, uploaded_by=uploader)
    add_book_to_fav(uploader_id,this_book.id)