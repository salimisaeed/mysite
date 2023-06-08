from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse("<h1>HOME PAGE</h1>")

def about_view(request):
    return JsonResponse({"Name" : "saeed", 
                         "LastName" : "salimi shad"})

def contact_view(request):
    return JsonResponse({"Phone": "09391701380"})