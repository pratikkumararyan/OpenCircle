from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.htmx and request.POST:
        print(request.POST)
        #HttpResponse(round((float(request.POST['rating'])/25)+1, 1))
        return render(request, "landingPage/partial.html")
    
    return render(request, 'landingPage/landing.html')

def account(request):
    return HttpResponse('This is the account creation page')
