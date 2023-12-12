from django.http import HttpResponse, JsonResponse

def http_test(Request):
    return HttpResponse('<h1>This Test For Http</h1>')

def json_test(Request):
    return JsonResponse({'name':'saeed'})