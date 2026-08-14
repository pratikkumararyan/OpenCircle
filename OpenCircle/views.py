from django.http import HttpResponse
from django.shortcuts import render, redirect
from ui.models import Suggestions
from email_validator import validate_email, EmailNotValidError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django_htmx.http import HttpResponseClientRedirect
from django.core.mail import send_mail
from django.conf import settings
import time, random
import threading

def index(request):
    # if request.user.is_authenticated:
    #     return redirect("/ui/")
    if request.htmx and request.POST:
        message = request.POST.get('message')
        rating = int(round((float(request.POST.get('rating'))/25)+1, 1))
        Suggestions.objects.create(rating=rating, message=message)
        return render(request, "landingPage/partial.html")
    
    return render(request, 'landingPage/landing.html')


def Login(request):
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
                return HttpResponseClientRedirect('/ui/')
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

def signupEmail(otpInt, emailId):
    send_mail("OpenCircle Signup OTP", "Your otp for Opencircle verification is " + otpInt, settings.EMAIL_HOST_USER, [emailId])

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
                issues.append("Username has already been taken.")
            except User.DoesNotExist:
                pass
            try:
                User.objects.get(email=email)
                issues.append("Duplicate e-mail detected.")
            except User.DoesNotExist:
                pass

            if issues == []:
                otpNumber = str(random.randint(1000, 9999))
                user = User.objects.create_user(username, email, password)
                user.first_name = "unverified"
                user.last_name = otpNumber
                user.save()
                userAuth = authenticate(request, username=username, password=password)
                login(request, userAuth)
                email_thread = threading.Thread(
                    target=signupEmail,
                    args=(otpNumber, email)
                )
                email_thread.start()
                return HttpResponseClientRedirect('/ui/')
        return render(request, "account/signup.html", {"issues": issues})
    return redirect("/")

def otpEmail(otpNumber, emailId):
    send_mail(f"Open Circle password reset attempt at your account", f"Hi there, there was recently a password reset attempt at the OpenCircle account associated with this email-id <i>[{emailId}]</i>. The OTP for the reset is <b>{otpNumber}</b> if this was you, or you can safely ignore this mail if it wasn't.", settings.EMAIL_HOST_USER, [emailId])

def forgot(request):
    if request.htmx: 
        issues = []
        if request.method == "POST":
            email = request.POST.get('email')
            try:
                User.objects.get(email=email)
                otpNumber = random.randint(1000, 9999)
                request.session['reset_otp'] = otpNumber
                request.session['reset_email'] = email

                email_thread = threading.Thread(
                                    target=otpEmail,
                                    args=(otpNumber, email)
                                )
                email_thread.start()
                
                return render(request, "account/otp.html")
            except User.DoesNotExist as e:
                issues.append(e)
                return render(request, "account/forgot.html", {"issues": issues, "email": email})

        elif request.method == "GET":
            return render(request, "account/forgot.html")
        
    return redirect("/")

def otp(request):
    if request.htmx:
        if request.method == "POST":
            otp = request.POST.get('otp')
            correctOtp = request.session.get('reset_otp')
            email = request.session.get('reset_email')

            if int(correctOtp) != int(otp):
                return render(request, "account/otp.html", {"incorrect": True})
            else:
                del request.session['reset_otp']
                return render(request, "account/reset.html")     
    return redirect("/")

def reset(request):
    if request.htmx: 
        if request.method == "POST":
            password = request.POST.get('passInput')
            email = request.session.get('reset_email')
            userObj = User.objects.get(email=email)
            userObj.set_password(password)
            userObj.save()
            return redirect("login")
            
    return redirect("/")

def Logout(request):
    logout(request)
    return redirect("/")
# FLOW FOR THE ACCOUNT PROCEDURE:
# 1. main landing page -> Get started
# 2. Modal opens-> If signup, then goes to /signup/ and then to /otp/ for the email otp
# 3. if login chosen, either normal simple login, OR:
#     forgot password -> forgot.html takes email -> otp.html takes OTP ->  correct otp -> reset.html takes new password -> auto-login + password reset
