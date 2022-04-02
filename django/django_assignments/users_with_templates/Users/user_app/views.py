import email
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from . import models

# Create your views here.

def index(request):
    list_of_users = models.list_of_all_users()
    print("-----------",list_of_all_users)
    context = {
        "users_list" : list_of_users,
    }
    return render(request,'index.html',context)

def user_info(request):
    # if request.method == "POST":
    #     user_name = request.POST['first_name']
    #     user_lastName = request.POST['last_name']
    #     user_email= request.POST['email']
    #     user_age = request.POST['age']

    #     User.objects.create(first_name=user_name, last_name=user_lastName, email=user_email,age=user_age)
        
        print("$$$$$$",request.POST)
        user_created = models.create_user(request.POST)

        return redirect("/")



## MVC 
    # MVC:    MODElS VIEWS CONTROLLERS
    # Django: Model.py  Templates Views.py MTV

