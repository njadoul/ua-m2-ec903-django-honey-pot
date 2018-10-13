from django import forms
from .models import Contact, Connex

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ConnexForm(forms.ModelForm):
    class Meta:
        model = Connex
        fields = '__all__'
