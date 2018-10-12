from django.shortcuts import render
from .forms import Contact

def contact(request):
    form = Contact(request.POST or None)
    if form.is_valide():
        nom = form.cleaned_data['nom']
        prénom = form.cleaned_data['prénom']
        mail = form.cleaned_data['mail']
        message = form.cleaned_data['message']

    return render(request, 'HoneyPot/contact.html', locals())
