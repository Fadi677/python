from multiprocessing import context
from this import d
from django.shortcuts import render, redirect
import random

def index(request):
    request.session['summation']=0
    context={
        'summation' : 0
    }
    print("--------")
    return render(request,'index.html',context)

def play(request):
    if request.POST['form_name'] == 'farm':
        # count=0
        if 'summation' in request.session:
            randomnum=random.randint(10, 20)
            request.session['summation']+=randomnum
        else:
            request.session['summation']=0
            print("_______",request.session['summation'])
            randomnum=random.randint(10, 20)
            request.session['summation']+=randomnum
            # count+=1
        context={
            'summation' : request.session['summation'],
            'money_info' : "Earned {} Golds from the Farm!".format(randomnum),
            # 'counter' : request.session['count']
        }
        return render(request,'index.html',context)
    
    elif request.POST['form_name'] == 'cave':
        if 'summation' in request.session:
            randomnum=random.randint(5, 10)
            request.session['summation']+=randomnum
        else:
            request.session['summation']=0
            print("_______",request.session['summation'])
            randomnum=random.randint(5, 10)
            request.session['summation']+=randomnum
        context={
            'summation' : request.session['summation'],
            'money_info' : "Earned {} Golds from the Cave!".format(randomnum)
            }
        return render(request,'index.html',context)

    elif request.POST['form_name'] == 'house':
        if 'summation' in request.session:
            randomnum=random.randint(2, 5)
            request.session['summation']+=randomnum
        else:
            request.session['summation']=0
            print("_______",request.session['summation'])
            randomnum=random.randint(2, 5)
            request.session['summation']+=randomnum
        context={
            'summation' : request.session['summation'],
            'money_info' : "Earned {} Golds from the House!".format(randomnum)
            }
        return render(request,'index.html',context)

    else:
        if 'summation' in request.session:
            randomnum=random.randint(-50, 50)
            request.session['summation']+=randomnum
        else:
            request.session['summation']=0
            print("_______",request.session['summation'])
            randomnum=random.randint(-50, 50)
            request.session['summation']+=randomnum
        if randomnum>0:
            context={
                'summation' : request.session['summation'],
                'money_info' : "Entered a Casino and earned {} Golds!".format(randomnum)
                }
        elif randomnum<0:
            x=abs(randomnum)
            context={
                'summation' : request.session['summation'],
                'money_info' : "Entered a Casino and Lost {} Golds!".format(x)
                }
        return render(request,'index.html',context)

def restartgame(request):
    return redirect('/')