from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('find',views.play),
    path('reset',views.restartgame)
]