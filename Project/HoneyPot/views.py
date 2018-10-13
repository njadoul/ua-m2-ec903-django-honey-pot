from django.shortcuts import render
from .forms import ContactForm, ConnexForm
from .models import Contact, Connex
import datetime


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        get_contact = Contact()
        get_contact.nom = form.cleaned_data['nom']
        get_contact.prénom = form.cleaned_data['prénom']
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

    return render(request, 'HoneyPot/contact.html', locals())


def connex(request):
    form = ConnexForm(request.POST or None)
    if form.is_valid():
        get_connex = Connex()
        get_connex.login = form.cleaned_data['login']
        get_connex.password = form.cleaned_data['password']

        get_connex.user_agent = request.META['HTTP_USER_AGENT']

        if ContactForm(request.POST):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')

            get_connex.ip = ipaddress
            get_connex.date = datetime.datetime.today()
            get_connex.save()

    return render(request, 'HoneyPot/connex.html', locals())

def home(request):
    return HttpResponse('<h1>Page login</h1>')
def conditions(request):
    return HttpResponse('<h1>Page conditions</h1>')
def donnees(request):
    return HttpResponse('<h1>Page donnees</h1>')
def mentions(request):
    return HttpResponse('<h1>Page mentions</h1>')
