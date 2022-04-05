from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from shows_app import models

def root(request):
    return redirect('/shows')

def index(request):
    context={
        'all_shows' : models.all_shows()
    }
    return render(request,'shows.html',context)

def new_show(request):
    return render (request,'add_show.html')

def add_show(request,postData):
    errors=models.ShowManager.basic_validator(postData)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows')
    else:
        this_show = models.create_show(postData)
        print("^^^^",this_show)
        return redirect('/shows/'+str(this_show.id))

def my_show(request,showid):
    context={
        'this_show' : models.get_show(showid)
    }
    return render(request,'my_show.html',context)

def edit_show(request,showid):
    context={
        'this_show' : models.get_show(showid)
    }
    return render(request,'editing.html',context)

def update_show(request):
    my_show_id=request.POST['show_id']
    show_to_update=models.update_me(request.POST,my_show_id)
    print("-------",show_to_update)
    return redirect('/shows/'+str(my_show_id))

def delete_show(request, showid):
    show_to_delete=models.delete_this(showid)
    return redirect('/shows')