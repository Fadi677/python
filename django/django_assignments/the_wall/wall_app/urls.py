from django.urls import path, include
from wall_app import views

urlpatterns = [
    path('',views.wall),#wall page localhost:8000/wall
    path('write',views.add_message),#adds a new message --> localhost:8000/wall/write
    path('write_comment',views.add_comment),#adds a new comment
    path('delete_comment',views.delete_this)
]