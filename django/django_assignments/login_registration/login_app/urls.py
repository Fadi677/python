from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),#landing page/main page
    path('register',views.registeration),#registration method
    path('success',views.success),#renders success page
    path('check_log',views.check),#checks log in information
    path('log_out',views.delete_session),#deletes user info from session and redirects to the root route
]