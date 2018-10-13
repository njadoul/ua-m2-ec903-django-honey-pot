from django import forms

class Contact(forms.Form):
    nom = forms.CharField(max_length = 50)
    prénom = forms.CharField(max_length = 50)
    mail = forms.EmailField(label="Votre adresse e-mail")
    message = forms.CharField(widget = forms.Textarea)

class Connex(forms.Form):
    login = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50)
