from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import django_htmx

def index(request):
    if request.htmx:
        print("smth")
        #return render(request, "Message Submitted! ")
        return HttpResponse('<input type="checkbox" id="my_modal_7" class="modal-toggle" />')
        #HttpResponse(round((float(request.POST['rating'])/25)+1, 1))
    
    return render(request, 'landingPage/landing.html')

def submitForm(request):
    if request.htmx and request.POST:
        print("it works!")
        return render(request, "landingPage/partial.html")
        
    return redirect('/')

def account(request):
    return HttpResponse('This is the account creation page')
