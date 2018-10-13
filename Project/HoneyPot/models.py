from django.db import models
from django.utils import timezone

class Connex(models.Model):
    login = models.TextField(max_length = 50, blank = True)
    password = models.TextField(max_length = 50, blank = True)
    ip = models.GenericIPAddressField()
    user_agent = models.TextField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date']
        verbose_name = "Formulaire de Login"

    def _str_(self):
        return self.ip

class Contact(models.Model):
    nom = models.TextField(max_length = 50, blank = True)
    prénom = models.TextField(max_length = 50, blank = True)
    mail = models.EmailField(max_length = 50, blank = True)
    message = models.TextField(max_length = 50, blank = True)
    ip = models.GenericIPAddressField()
    user_agent = models.TextField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date']
        verbose_name = "Formulaire de Contact"

    def _str_(self):
        return self.ip
