from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Page login</h1>')

def contact(request):
    return HttpResponse('<h1>Page contact</h1>')

def conditions(request):
    return HttpResponse('<h1>Page conditions</h1>')

def donnees(request):
    return HttpResponse('<h1>Page donnees</h1>')

def mentions(request):
    return HttpResponse('<h1>Page mentions</h1>')
