from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def ui(request):
    user = request.user
    name = user.username
    profile = Profile.objects.get(user=user)
    img = profile.profile_picture.url
    following = user.followers.all()
    return render(request, "UI/dashboard.html", {"username": name, "img": img, "following": following})

@login_required
def post(request):
    return HttpResponse('Post site here')

@login_required
def accountPage(request, UserId):
    user = User.objects.get(pk=UserId)
    return render(request, "UI/profile.html", {"user": user})

@login_required
def dm(request):
    return HttpResponse('DM site here')

@login_required
def friends(request):
    return HttpResponse('Friends list here')

def postMessage(request):
    if request.htmx and request.POST:
        message = request.POST.get("htmlField")
        image = request.POST.get("fileInput")
        if len(message) > 4500:
            return HttpResponse('<p class="text-md text-error">Message too long! Please shorten it.</p>')
        if image.split('.')[-1] != "png":
            return HttpResponse('<p class="text-md text-error">Please upload a PNG image only..</p>')
        Post.objects.create(poster=request.user, content=message, image=image)
        return HttpResponse('<p class="text-md text-success">Message successfully posted!</p>')
    return redirect("/")