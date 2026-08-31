from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
import pytesseract
from PIL import Image
from django_htmx.http import HttpResponseClientRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
MAX_IMAGE_SIZE = 500 * 1024 

@login_required
def ui(request):
    user = request.user
    following = user.followers.all()
    newest = Post.objects.all().order_by("-timestamp")[0].pk
    return render(request, "UI/dashboard.html", {"user": user, "following": following, "newest": newest})


@login_required
def accountPage(request, UserId):
    if request.POST:
        isFollowing = request.POST.get("isFollowing")
        targetId = request.POST.get("targetId")
        targetUser = User.objects.get(pk=targetId)
        targetProfile = targetUser.profile
        if isFollowing == "True":
            targetProfile.followers.remove(request.user)
        else:
            targetProfile.followers.add(request.user)
    user = User.objects.get(pk=UserId)
    allPosts = Post.objects.filter(poster=user)
    newest = allPosts.order_by("timestamp").count()
    print(newest)
    nPosts = allPosts.count
    isUser = (user == request.user)
    allFollowers = user.profile.followers
    isFollowing = False
    if not isUser:
        isFollowing = allFollowers.contains(request.user)
    nFollowing = allFollowers.count
    nFollowers = user.followers.count
    return render(request, "UI/profile.html", {"user": user, "newest": newest, "nPosts": nPosts, "nFollowers": nFollowers, "nFollowing": nFollowing, "isUser": isUser, "isFollowing": isFollowing})


def postMessage(request):
    if request.htmx and request.POST:
        message = request.POST.get("htmlField")
        print(message)
        if len(message) > 4500:
            return HttpResponse('<p class="text-md text-error">Message too long! Please shorten it.</p>')
        try:
            image = request.FILES.get("fileInput")
            if image.size <= MAX_IMAGE_SIZE:
                Post.objects.create(poster=request.user, content=message, image=image)
            else:
                return HttpResponse("File too big.")
        except:
            Post.objects.create(poster=request.user, content=message)
        return HttpResponseClientRedirect('/ui/')
    return redirect("/")

def feed(request, postId):
    lastIndex = str(int(request.GET.get(f"post{postId}")) - 1)
    try:
        postObj = Post.objects.get(pk=postId)
        return render(request, "UI/postPartial.html", {"post": postObj, "Id": lastIndex})
    except Post.DoesNotExist:
        return HttpResponse("<p class='-m-2 text-error'><center>That's it for today!</center></p>")

def profileFeed(request, postId):
    lastIndex = postId
    userId = request.GET.get("userId")
    try:
        userObj = User.objects.get(pk=userId)
        allPosts = Post.objects.filter(poster=userObj)
        postObj = allPosts.order_by("timestamp")[lastIndex-1]
        return render(request, "UI/profilePartial.html", {"post": postObj, "Id": lastIndex-1})
    except:
        return HttpResponse("")

def exit(request):
    logout(request)
    return redirect("/")

@csrf_exempt
def bioUpdate(request):
    if request.htmx and request.POST:
        bio = request.POST.get("content", '').strip()
        userProfile = request.user.profile
        userProfile.bio = bio
        userProfile.save()
        return HttpResponse(bio)

def accountValidate(request):
    if request.htmx and request.POST:
        otp = request.POST.get("otp")
        img = request.FILES.get("fileInput")
        user = request.user
        if img.size > MAX_IMAGE_SIZE:
            return HttpResponse("Image must be <500 KB.")
        else:
            if int(otp) == int(user.last_name):
                profile = user.profile
                profile.medical_cert = img
                profile.save()
                user.first_name = "verified"
                user.save()
                return HttpResponse("Your medical cert is still yet to be verified, but you can post now! (You need to reload first)")
            else:
                return HttpResponse("Incorrect OTP!")
    return redirect("/")