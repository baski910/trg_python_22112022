from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Welcome to Django app</h1>")
    #msg = 'Test Message'
    #return render(request,"simpleapp/index.html",{'message': msg })
    #names = ['tom','pat','raj']
    #return render(request,"simpleapp/index.html",{'names': names })
    names = [{'name':'bob'},{'name':'sam'},{'name':'vas'}]
    return render(request,"simpleapp/index.html",{'names': names })

def getParams(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect(reverse('simpleapp:index'))
