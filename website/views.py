from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(Request):
    return render(Request, 'website/index.html')

def about_view(Request):
    return render(Request, 'website/about.html')

def contact_view(Request):
    return render(Request, 'website/contact.html')
