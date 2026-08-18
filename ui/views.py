from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ui(request):
    user = request.user
    name = user.username
    print(name)
    profile = Profile.objects.get(user=user)
    img = profile.profile_picture
    return render(request, "UI/dashboard.html", {"username": name, "img": img})

@login_required
def post(request):
    return HttpResponse('Post site here')

@login_required
def dm(request):
    return HttpResponse('DM site here')

@login_required
def friends(request):
    return HttpResponse('Friends list here')