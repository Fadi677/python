from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),  
    path('destroy_session',views.destroyme),
    path('plus2',views.add2),
    path('useradd',views.addnumber),
]