from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(Request):
    return render(Request, 'website/index.html')

def about_view(Request):
    return render(Request, 'website/about.html')

def contact_view(Request):
    return render(Request, 'website/contact.html')

def elements_view(Request):
    return render(Request, 'website/elements.html')

def test_view(Request):
    return render(Request, 'website/test.html',{'name':'sorena','last_name':'salimi'})
