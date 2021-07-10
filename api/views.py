from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.



def users(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    if id is None:
        return JsonResponse({"sucess":"False", "message":"id is null"})
    if name is None:
        return JsonResponse({"sucess":"False", "message":"name is null"})
    user = {"id":id,"name":name}
    return JsonResponse({"sucess":"True", "message":"user info","data":user})