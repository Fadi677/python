from django.shortcuts import render, redirect,HttpResponse
from ninjas_app import models

def index(request):
    context={
        'list_of_dojos':models.all_dojos()
    }
    return render(request,'dojos.html',context)

def adddojo(request):
    print(request.POST)
    models.create_dojo(request.POST['name'],request.POST['city'],request.POST['state'])
    return redirect('/')

def addNinja(request):
    print(type(request.POST['dojo_list']))
    models.getDojo(request.POST['first_name'],request.POST['last_name'],int(request.POST['dojo_list']))
    return redirect('/')