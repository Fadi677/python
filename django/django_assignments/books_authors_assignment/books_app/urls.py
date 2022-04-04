from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook',views.addbook),
    path('authors',views.authors),
    path('addauthor',views.addauthor),
    path('books/<int:bookid>',views.showbook),
    path('authors/<int:authorid>',views.showauthor)
]