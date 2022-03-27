from django.shortcuts import render

def index(request):
    return render(request,'survey.html')


def showresult(request):
    name=request.POST['name']
    location=request.POST['location']
    language=request.POST['language']
    comment=request.POST['comment']

    context={
        'name':name,
        'location':location,
        'language':language,
        'comment':comment
    }
    return render(request,'show.html',context)