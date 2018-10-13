from django import forms
from .models import Contact, Connex

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('nom', 'prénom', 'mail', 'message')

class ConnexForm(forms.ModelForm):
    class Meta:
        model = Connex
        fields = ('login', 'password')
