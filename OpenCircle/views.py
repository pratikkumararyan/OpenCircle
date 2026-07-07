from django.http import HttpResponse
from django.shortcuts import render
from ui.models import Suggestions

def index(request):
    if request.htmx and request.POST:
        message = request.POST.get('message')
        rating = int(round((float(request.POST.get('rating'))/25)+1, 1))
        Suggestions.objects.create(rating=rating, message=message)
        return render(request, "landingPage/partial.html")
    
    return render(request, 'landingPage/landing.html')

def account(request):
    return render(request, 'account/account.html')
