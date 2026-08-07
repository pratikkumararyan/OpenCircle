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
        nature = request.POST.get('nature')
        if nature == "login":
            user = request.POST.get('username')
            password = request.POST.get('passInput')

            errors = ["hmm heres a test error 1", "another error 2", "holy moly error 3 asw"]
            return render(request, "account/login.html", {"issues": errors})
        elif nature == "signup":
            return render(request, "account/signup.html", {"issues": errors})
        

    return redirect("/")

def signup(request):
    if request.htmx:
        return render(request, "account/signup.html")
    return redirect("/")

def forgot(request):
    if request.htmx:
        return render(request, "account/forgot.html")
    return redirect("/")

def otp(request):
    if request.htmx:
        return render(request, "account/otp.html")
    return redirect("/")

def reset(request):
    if request.htmx:
        return render(request, "account/reset.html")
    return redirect("/")
