from django.shortcuts import render
from .forms import ContactForm
from .forms import ConnexForm

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valide():
        nom = form.cleaned_data['nom']
        prénom = form.cleaned_data['prénom']
        mail = form.cleaned_data['mail']
        message = form.cleaned_data['message']

    return render(request, 'HoneyPot/contact.html', locals())


def connex(request):
    form = ConnexForm(request.POST or None)
    if form.is_valide():
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']

    return render(request, 'HoneyPot/connex.html', locals())
