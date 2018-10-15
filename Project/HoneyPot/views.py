
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm, ConnexForm
from .models import Contact, Connex
from django.http import HttpReponseRedirect

import datetime


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        get_contact = Contact()
        get_contact.nom = form.cleaned_data['nom']
        get_contact.prenom = form.cleaned_data['prenom']
        get_contact.mail = form.cleaned_data['mail']
        get_contact.message = form.cleaned_data['message']


        get_contact.user_agent = request.META['HTTP_USER_AGENT']

        if ContactForm(request.POST):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')

            get_contact.ip = ipaddress
            get_contact.date = datetime.datetime.today()
            get_contact.save()

            res = send_mail(get_contact.nom, get_contact.message, get_contact.message, ['loicjeancharles@gmail.com','nathanjadoul@live.fr'], fail_silently=False)

            if res:
                messages.success(request, 'Message envoyé')
            else:
                messages.error(request, 'Message non envoyé')
            
            return http.HttpReponseRedirect('')

    return render(request, 'HoneyPot/contact.html', locals())


def home(request):
    form = ConnexForm(request.POST or None)
    if form.is_valid():
        get_connex = Connex()
        get_connex.login = form.cleaned_data['login']
        get_connex.password = form.cleaned_data['password']

        get_connex.user_agent = request.META['HTTP_USER_AGENT']

        if ConnexForm(request.POST):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')

            get_connex.ip = ipaddress
            get_connex.date = datetime.datetime.today()
            get_connex.save()

            # user = authenticate(username=get_connex.login, password=get_connex.password)

            # if user:
                # login(request, user)
                # messages.success(request, 'Connexion réussie')
            # else:
            messages.error(request, 'La connexion a échouée')

    return render(request, 'HoneyPot/login.html', locals())

# Create your views here.
# def home(request):
#     return render(request,'HoneyPot/login.html', { 'title' : 'Se connecter'})

# def contact(request):
#     return render(request,'HoneyPot/contact.html', { 'title' : 'Nous contacter'})

def conditions(request):
    return render(request,'HoneyPot/conditions.html', { 'title' : 'Conditions d\'utilisations'})

def donnees(request):
    return render(request,'HoneyPot/donnees.html', { 'title' : 'Données personnelles'})
  
def mentions(request):
    return render(request,'HoneyPot/mentions.html', { 'title' : 'Mentions légales'})

