from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'HoneyPot/login.html', { 'title' : 'Se connecter'})

def contact(request):
    return render(request,'HoneyPot/contact.html', { 'title' : 'Nous contacter'})

def conditions(request):
    return render(request,'HoneyPot/conditions.html', { 'title' : 'Conditions d\'utilisations'})

def donnees(request):
    return render(request,'HoneyPot/donnees.html', { 'title' : 'Données personnelles'})

def mentions(request):
    return render(request,'HoneyPot/mentions.html', { 'title' : 'Mentions légales'})
