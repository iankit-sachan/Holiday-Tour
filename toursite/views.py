from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Tour Site!")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About the Tour Site")

def contact(request): 
    return HttpResponse("Contact Us at the Tour Site")

def services(request):
    return HttpResponse("Our Services at the Tour Site")

def faq(request):
    return HttpResponse("Frequently Asked Questions at the Tour Site")

def gallery(request):
    return HttpResponse("Gallery of the Tour Site")