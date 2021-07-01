from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    name = request.GET.get("name")
    return HttpResponse("hello " + name)

def calculator(request):
    """
    计算器视图
    """
    return(render(request, "calculator.html"))