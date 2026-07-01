from django.http import HttpResponse
from django.shortcuts import render
import django_htmx

def index(request):
    if request.htmx:
        print("smth")
        #return render(request, "Message Submitted! ")
        return HttpResponse('<input type="checkbox" id="my_modal_7" class="modal-toggle" />')
        #HttpResponse(round((float(request.POST['rating'])/25)+1, 1))
    
    return render(request, 'landing.html')

def account(request):
    return HttpResponse('This is the account creation page')
