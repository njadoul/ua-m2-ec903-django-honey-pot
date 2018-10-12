from django import forms

class Contact(forms.Form):
    nom = models.CharField(max_length = 50)
    prénom = models.CharField(max_length = 50)
    mail = models.EmailField(label="Votre adresse e-mail")
    message = models.CharField(widget = forms.Textarea)
