from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from users_app import models
from users_app.models import User
from books_app.urls import *
import bcrypt


def root(request):
    return render(request,'landing.html')

def registeration(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        create_new=models.create_u(request.POST)
        request.session['id']=create_new.id
        request.session['first_name'] = create_new.first_name
        request.session['last_name']=create_new.last_name
        request.session['email']=create_new.email
        return redirect('/books')

def check(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        logged_user = models.log_in_u(request.POST['email'])
        if logged_user:
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_in']=True
                request.session['email']=logged_user.email
                request.session['id']=logged_user.id
                request.session['first_name']=logged_user.first_name
                request.session['last_name']=logged_user.last_name
                return redirect('/books') #localchost:8000/wall/
        else:
            return redirect('/')

def delete_session(request):
    request.session.flush()
    return redirect('/')