from django.shortcuts import render, redirect
import random

def index(request):
    return render(request,'index.html')

def play(request):
    if request.POST['form_name'] == 'farm':
        if 'summation' in request.session:
            randomnum=random.randint(10, 20)
            request.session['summation']+=randomnum
            context={
                'summation' : request.session['summation']
            }
            print("++++++",randomnum,context['summation'])
            return render(request,'index.html',context)
        else:
            request.session['summation']=0
            print("_______",request.session['summation'])
            randomnum=random.randint(10, 20)
            request.session['summation']+=randomnum
            context={
                'summation' : request.session['summation']
            }
            print("------",randomnum,context['summation'])
            return render(request,'index.html',context)