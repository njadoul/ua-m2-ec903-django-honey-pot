from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'HoneyPot/login.html')

def contact(request):
    return render(request,'HoneyPot/contact.html')

def conditions(request):
    return render(request,'HoneyPot/conditions.html')

def donnees(request):
    return render(request,'HoneyPot/donnees.html')

def mentions(request):
    return render(request,'HoneyPot/mentions.html')
