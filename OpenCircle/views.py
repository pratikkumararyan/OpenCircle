from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.META.get("HTTP_HTMX_REQUEST"):
        print("smth")
        #return render(request, "Message Submitted! ")
        return HttpResponse('<input type="checkbox" id="my_modal_7" class="modal-toggle" />')
        #HttpResponse(round((float(request.POST['rating'])/25)+1, 1))
    else:
        return render(request, 'landing.html')

def account(request):
    return HttpResponse('This is the account creation page')
