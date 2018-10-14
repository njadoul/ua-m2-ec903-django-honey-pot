from django.db import models
from django.utils import timezone

class Connex(models.Model):
    login = models.CharField(max_length = 20, blank = True)
    password = models.CharField(max_length = 20, blank = True)
    ip = models.GenericIPAddressField()
    user_agent = models.TextField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Formulaire de Login"

    def _str_(self):
        return self.ip

class Contact(models.Model):
    nom = models.CharField(max_length = 20, blank = True)
    prenom = models.CharField(max_length = 20, blank = True)
    mail = models.EmailField(blank = True)
    message = models.TextField(max_length = 50, blank = True)
    ip = models.GenericIPAddressField()
    user_agent = models.TextField(max_length = 50)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Formulaire de Contact"

    def _str_(self):
        return self.ip
