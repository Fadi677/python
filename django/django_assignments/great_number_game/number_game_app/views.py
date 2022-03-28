from unittest import result
from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    randomnum=random.randint(1, 100)
    request.session['systemnum']=randomnum
    print("++++++++++++",request.session['systemnum'])
    return render(request,"game_page.html")

def gamestart(request):
    if (int(request.POST['myguess'])==request.session['systemnum']):
        context={'result' : f"{request.session['systemnum']} is Correct!"}
        return render(request,"game_page.html",context)
    elif (int(request.POST['myguess'])>request.session['systemnum']):
        context={'result': "Too High"}
        return render(request,"game_page.html",context)
    else:
        context={'result':"Too Small"}
        return render(request,"game_page.html",context)