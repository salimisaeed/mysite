from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(Request):
    return HttpResponse('<h1>Home Page</h1>')

def about_view(Request):
    return HttpResponse('<h1>About Page</h1>')

def contact_view(Request):
    return HttpResponse('<h1>Contact Page</h1>')
