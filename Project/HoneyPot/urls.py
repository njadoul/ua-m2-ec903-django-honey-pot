from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact/', views.contact, name = 'contact'),
    path('conditions/', views.conditions, name = 'conditions'),
    path('mentions/', views.mentions, name = 'mentions'),
    path('donnees/', views.donnees, name = 'donnees'),
]
