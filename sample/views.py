from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse


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
    接口：计算
    """
    num1 = request.GET.get("number1","")
    num2 = request.GET.get("number2","")
    if num1 == "" or num2 == "":
        return JsonResponse({"code":"10101","message":"参数不能为空", "data":[]})
    try:
        result = int(num1) + int(num2)
    except ValueError:
        return JsonResponse({"code":"10102","message":"请输入数字", "data":[]})
    return JsonResponse({"code":"10200","message":"成功", "data":ret})
