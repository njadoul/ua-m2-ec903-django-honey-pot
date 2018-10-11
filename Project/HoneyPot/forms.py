from django import forms
from django.contib.auth.forms import UserCreationForm
from django.contib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text = 'Format attendu : AAAA-MM-JJ')

    class Meta:
        model = User
        field = ('username', 'birt_date', 'password1', 'password2',)
