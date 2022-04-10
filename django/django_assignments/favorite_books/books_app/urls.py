from django.urls import path, include
from books_app import views

urlpatterns = [
    path('',views.books_page),#main books page
    path('add',views.add_book),
    path('add_fav',views.add_to_fav)
]