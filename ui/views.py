from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ui(request):
    return HttpResponse('UI Site with recommendations etc.')

def post(request):
    return HttpResponse('Post site here')

def dm(request):
    return HttpResponse('DM site here')

def friends(request):
    return HttpResponse('Friends list here')