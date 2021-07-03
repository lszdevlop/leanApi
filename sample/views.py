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
    if request.method == "GET":
        return render(request, "calculator.html")
    if request.method == "POST":
        num1 = request.POST.get("number1")
        num2 = request.POST.get("number2")
        if num1 == "" or num2 == "":
            return HttpResponse("不能为空")
        try:
            result = int(num1) + int(num2)
        except ValueError:
            return HttpResponse("请输入数字")
        return HttpResponse(result)

def calculate(request):
    """
    计算
    """
    # num1 = request.GET.get("number1")
    # num2 = request.GET.get("number2")
    # if num1 == "" or num2 == "":
    #     return HttpResponse("不能为空")
    # try:
    #     result = int(num1) + int(num2)
    # except ValueError:
    #     return HttpResponse("请输入数字")
    # return HttpResponse(result)
