from django.contrib import admin
from .models import Contact, Connex

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['ip', 'date']
    ordering = ['date']

@admin.register(Connex)
class ConnexAdmin(admin.ModelAdmin):
    list_display = ['ip', 'date']
    ordering = ['date']
