from django.db import models
from django.utils import timezone

class Profil(models.Model):
    login = models.TextField(max_length = 50)
    password = models.TextField(max_length = 50)
    ip = models.TextField(max_length = 50)
    user_agent = models.TextField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date']
        verbose_name = "Formulaire de Login"

    def _str_(self):
        return self.ip

class Contact(models.Model):
    nom = models.TextField(max_length = 50)
    prénom = models.TextField(max_length = 50)
    mail = models.EmailField(max_length = 50)
    message = models.TextField(max_length = 50)
    ip = models.TextField(max_length = 50)
    user_agent = models.TextField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date']
        verbose_name = "Formulaire de Contact"

    def _str_(self):
        return self.ip
