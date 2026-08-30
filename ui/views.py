from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.

@login_required
def ui(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    img = profile.profile_picture.url
    following = user.followers.all()
    newest = Post.objects.all().order_by("-timestamp")[0].pk
    return render(request, "UI/dashboard.html", {"user": user, "following": following, "newest": newest})

@login_required
def post(request):
    return HttpResponse('Post site here')


def accountPage(request, UserId):
    user = User.objects.get(pk=UserId)
    allPosts = Post.objects.filter(poster=user)
    newest = allPosts.order_by("-timestamp")[0].pk
    nPosts = allPosts.count
    nFollowing = user.profile.followers.count
    nFollowers = user.followers.count
    return render(request, "UI/profile.html", {"user": user, "newest": newest, "nPosts": nPosts, "nFollowers": nFollowers, "nFollowing": nFollowing})

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

def feed(request, postId):
    lastIndex = str(int(request.GET.get(f"post{postId}")) - 1)
    try:
        postObj = Post.objects.get(pk=postId)
        return render(request, "UI/postPartial.html", {"post": postObj, "Id": lastIndex})
    except Post.DoesNotExist:
        return HttpResponse("<p class='-m-2 text-error'><center>That's it for today!</center></p>")

def exit(request):
    logout(request)
    return redirect("/")
    
    