from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"intro/index.html")

def calculator(request):
    return HttpResponse("calculator page")


def measurer(request):
    return render(request,"intro/measurer.html")

def test(request , name):
    return render(request,"intro/test.html",{
    "name" : name.capitalize()
    })
    




