from django.shortcuts import render

def index(request):
    return render(request,'survey.html')


def showresult(request):
    # name=request.POST['name']
    location=request.POST['location']
    language=request.POST['language']
    comment=request.POST['comment']

    context={
        'name':request.POST['name'],
        'location':request.POST['location'],
        'language':request.POST['language'],
        'comment':request.POST['comment']
    }
    return render(request,'show.html',context)