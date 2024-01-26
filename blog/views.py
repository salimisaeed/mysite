from django.shortcuts import render

# Create your views here.

def blog_view(Request):
    return render(Request, 'blog/blog-home.html')

def blog_single(Request ):
    return render(Request, 'blog/blog-single.html')

