from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def account(request):
    return HttpResponse('This is the account creation page')

