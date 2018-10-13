from django.shortcuts import render
from .forms import ContactForm, ConnexForm
from .models import Contact, Connex
import datetime


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valide():
        nom = form.cleaned_data['nom']
        prénom = form.cleaned_data['prénom']
        mail = form.cleaned_data['mail']
        message = form.cleaned_data['message']

        user_agent = request.META.get['HTTP_USER_AGENT']

        if ContactForm(request.POST):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')
            get_ip = Contact()
            ip = ipaddress
            date = datetime.date.today()
            #get_ip.save()

    return render(request, 'HoneyPot/contact.html', locals())


def connex(request):
    form = ConnexForm(request.POST or None)
    if form.is_valide():
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']

        user_agent = request.META.get['HTTP_USER_AGENT']

        if ContactForm(request.POST):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')
            get_ip = Connex()
            ip = ipaddress
            date = datetime.date.today()
            #get_ip.save()

    return render(request, 'HoneyPot/connex.html', locals())
