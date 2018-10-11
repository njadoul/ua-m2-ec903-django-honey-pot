from django.db import models

class Profil(models.Model):
    login = models.TextField(max_length = 50)
    password = models.TextField(max_length = 50)
    nom = models.TextField(max_length = 50)
    prénom = models.TextField(max_length = 50)
    mail = models.EmailField(max_length = 50)
    message = models.TextField(max_length = 50)
