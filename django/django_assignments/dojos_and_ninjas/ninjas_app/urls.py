from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('addingdojo',views.adddojo),
    path('addNinja', views.addNinja),
]