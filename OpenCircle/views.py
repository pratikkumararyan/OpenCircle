from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        
        return HttpResponse(round((float(request.POST['rating'])/25)+1, 1))
    else:
        return render(request, 'landing.html')

def account(request):
    return HttpResponse('This is the account creation page')

# 4 -> 75, 
# 5 -> 100, 
# 1 -> 0, 
# 3 -> 50