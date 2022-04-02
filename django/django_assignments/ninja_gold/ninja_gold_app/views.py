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
        if 'summation' in request.session:
            randomnum=random.randint(10, 20)
            request.session['summation']+=randomnum
        else:
            request.session['summation']=0
            print("_______",request.session['summation'])
            randomnum=random.randint(10, 20)
            request.session['summation']+=randomnum
        context={
            'summation' : request.session['summation'],
            'money_info' : "Earned {} Golds from the Farm!".format(randomnum)
        }
        print("------",context.keys,context.values)
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
        else:
            context={
                'summation' : request.session['summation'],
                'money_info' : "Entered a Casino and didn't win or lose any Golds!"
                }
        return render(request,'index.html',context)

def restartgame(request):
    return redirect('/')