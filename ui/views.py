from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ui(request):
    return render(request, "UI/dashboard.html")

@login_required
def post(request):
    return HttpResponse('Post site here')

@login_required
def dm(request):
    return HttpResponse('DM site here')

@login_required
def friends(request):
    return HttpResponse('Friends list here')