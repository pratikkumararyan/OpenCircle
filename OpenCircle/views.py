from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        print(request.POST)
    else:
        return render(request, 'landing.html')

def account(request):
    return HttpResponse('This is the account creation page')

