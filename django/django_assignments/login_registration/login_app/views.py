from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from login_app import models
from .models import User
import bcrypt


def root(request):
    return render(request,'login.html')

def registeration(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        create_new=models.create_u(request.POST)
        request.session['name'] = create_new.first_name
        request.session['id']=create_new.id
        return redirect('/success')


def success(request):
    
    context={
        'user_info' : models.get_user(request.session['id'])
    }
    return render(request,'success.html',context)

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
                request.session['email']=logged_user.email
                request.session['id']=logged_user.id
                request.session['name']=logged_user.first_name
                return redirect('/success')
        else:
            return redirect('/')

def delete_session(request):
    request.session.clear()
    return redirect('/')