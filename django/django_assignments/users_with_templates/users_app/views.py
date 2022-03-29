from django.shortcuts import render, redirect
from .models import users

def index(request):
    context={
        "all_users" : users.objects.all()
    }
    return render(request, "users.html", context)

def showusers(request):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    emailaddress=request.POST['email']
    age=int(request.POST['age'])
    users.objects.create(first_name=firstname,last_name=lastname,email_address=emailaddress,age=age)

    return redirect('/')