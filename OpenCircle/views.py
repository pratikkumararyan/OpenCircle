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
        issues = []
        if str(request.method) == "GET":
            issues = []
        else:
            issues.append("why using post")
        return render(request, "account/login.html", {"issues": issues})
    return redirect("/")

def authenticate(request):
    # if request.htmx and request.POST:
    #     nature = request.POST.get('nature')
    #     if nature == "login":
    #         user = request.POST.get('username')
    #         password = request.POST.get('passInput')

    #         errors = ["hmm heres a test error 1", "another error 2", "holy moly error 3 asw"]
    #         return render(request, "account/login.html", {"issues": errors})
    #     elif nature == "signup":
    #         return render(request, "account/signup.html", {"issues": errors})
        

    return redirect("/")

def signup(request):
    if request.htmx:
        issues = []
        if request.method == "GET":
            pass
        elif request.method == "POST":
            issues.append("bro imagine using post")
        return render(request, "account/signup.html", {"issues": issues})
    return redirect("/")

def forgot(request):
    if request.htmx and request.POST:
        return render(request, "account/forgot.html")
    return redirect("/")

def otp(request):
    if request.htmx and request.POST:
        otp = request.POST.get('otp')
        print(otp)
        return render(request, "account/otp.html", {"incorrect": True})
    return redirect("/")

def reset(request):
    if request.htmx and request.POST:
        print("resettin' the password")
    return redirect("/")

# FLOW FOR THE ACCOUNT PROCEDURE:
# 1. main landing page -> Get started
# 2. Modal opens-> If signup, then goes to /signup/ and then to /otp/ for the email otp
# 3. if login chosen, either normal simple login, OR:
#     forgot password -> forgot.html takes email -> otp.html takes OTP ->  correct otp -> reset.html takes new password -> auto-login + password reset
