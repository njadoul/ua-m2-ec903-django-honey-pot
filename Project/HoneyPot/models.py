from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Profil(models.Models):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.TextField(max_length = 50, blank = True)
    last_name = models.TextField(max_length = 50, blank = True)
    bio = models.TextField(max_length = 500, blank = True)
    birth_date = models.DateField(null = True, blank = True)

@receiver(post_save, sender = User)
def update_user_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user = instance)
    instance.profil.save()

class Contact(models.Model):
