from django.http import HttpResponse
from django.shortcuts import render, redirect
from ui.models import Suggestions

def index(request):
    if request.htmx and request.POST:
        message = request.POST.get('message')
        rating = int(round((float(request.POST.get('rating'))/25)+1, 1))
        Suggestions.objects.create(rating=rating, message=message)
        return render(request, "landingPage/partial.html")

    return render(request, 'landingPage/landing.html')


def login(request):
    if request.htmx:
        return render(request, "account/login.html", {"issues": []})
    return redirect("/")

def authenticate(request):
    if request.htmx and request.POST:
        user = request.POST.get('username')
        password = request.POST.get('passInput')
        errors = ["hmm heres a test error 1", "another error 2", "holy moly error 3 asw"]
        return render(request, "account/login.html", {"issues": errors})

    return redirect("/")

def signup(request):
    if request.htmx:
        return render(request, "account/signup.html")
    return redirect("/")

def forgot(request):
    return redirect("/")

def otp(request):
    return redirect("/")
