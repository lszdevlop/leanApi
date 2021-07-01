from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def hello(request):
    name = request.GET.get("name")
    return HttpResponse("hello " + name)

def user(request, id):
    print(id)
    return HttpResponse("userid " + str(id))
