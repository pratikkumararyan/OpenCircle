from django.http import HttpResponse
from django.shortcuts import render, redirect
from ui.models import Suggestions
from email_validator import validate_email, EmailNotValidError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import time

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
        if request.method == "GET":
            issues = []
        elif request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('passInput')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/ui/")
            else:
                issues.append("Invalid username or password.")

        return render(request, "account/login.html", {"issues": issues})
    return redirect("/")

def change(request):
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
            username = request.POST.get('username')
            email = request.POST.get('email')
            try:
                validate_email(email)
            except EmailNotValidError as e:
                issues.append(e)
            password = request.POST.get('passInput')
            try:
                User.objects.get(username=username)
                User.objects.get(email=email)
                issues.append("Duplicate email/username detected.")
            except User.DoesNotExist:
                pass
            if issues == []:
                user = User.objects.create_user(username, email, password)
                user.first_name = "unverified"
                user.last_name = "1111"
                user.save()
                time.sleep(1)
                userAuth = authenticate(request, username=username, password=password)
                login(request, userAuth)
                return redirect("/ui/")
        return render(request, "account/signup.html", {"issues": issues})
    return redirect("/")

def forgot(request):
    if request.htmx: 
        issues = []
        if request.method == "POST":
            email = request.POST.get('email')
            try:
                validate_email(email)
                #send otp to e-mail here
                return render(request, "account/otp.html", {"nature": "reset"})
            except EmailNotValidError as e:
                issues.append(e)
                return render(request, "account/forgot.html", {"issues": issues, "email": email})

        elif request.method == "GET":
            return render(request, "account/forgot.html")
        
    return redirect("/")

def otp(request):
    if request.htmx:
        if request.POST:
            print("wait this also works")
        if request.method == "POST":
            otp = request.POST.get('otp')
            correctOtp = 1111

            
    return redirect("/")

def reset(request):
    if request.htmx: 
        if request.method == "POST":
            print("resettin' the password")
    return redirect("/")

# FLOW FOR THE ACCOUNT PROCEDURE:
# 1. main landing page -> Get started
# 2. Modal opens-> If signup, then goes to /signup/ and then to /otp/ for the email otp
# 3. if login chosen, either normal simple login, OR:
#     forgot password -> forgot.html takes email -> otp.html takes OTP ->  correct otp -> reset.html takes new password -> auto-login + password reset
