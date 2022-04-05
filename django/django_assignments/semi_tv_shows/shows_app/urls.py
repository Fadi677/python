from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.root),
    path('shows', views.index), #goes to shows table
    path('shows/new', views.new_show), #goes to adding new show page
    path('shows/create',views.add_show), #creates new show
    path('shows/<int:showid>',views.my_show), #displays the selected show
    path('shows/<int:showid>/edit',views.edit_show), #displayes the editing page
    path('update_show_info',views.update_show), #redirects to the update method
    path('shows/<int:showid>/delete',views.delete_show) #deletes the displayed show in edit page
]