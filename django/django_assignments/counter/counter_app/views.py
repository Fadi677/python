from django.shortcuts import render, redirect

# def index(request):
#     return render('counter.html')

def index(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter']=1
    
    return render(request,'counter.html')

def destroyme(request):
    if 'counter' in request.session:
        request.session['counter']=1
    return render(request,'counter.html')

def add2(request):
    if 'counter' in request.session:
        request.session['counter']+=2
    else:
        request.session['counter']=0
    
    return render(request,'counter.html')

def addnumber(request):
    if 'counter' in request.session:
        print(type(request.session['counter'])) #int
        request.session['counter']+=int(request.POST['numbertoadd'])
    else:
        request.session['counter']=0
    
    return render(request,'counter.html')