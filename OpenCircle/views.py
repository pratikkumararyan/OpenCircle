from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Suggestions

def index(request):
    if request.htmx and request.POST:
        print("htmx+POST request received")
        message = request.POST.get('message')
        rating = int(round((float(request.POST.get('rating'))/25)+1, 1))
        # entry = Suggestions.objects.create(rating=rating, message=message)
        # print(Suggestions.objects.values_list("message", flat=True))
        return render(request, "landingPage/partial.html")
    
    return render(request, 'landingPage/landing.html')

def account(request):
    return HttpResponse('This is the account creation page')
