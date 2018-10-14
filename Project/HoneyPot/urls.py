from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('', auth_views.LoginView.as_view(template_name='HoneyPot/login.html'), name = 'home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='HoneyPot/logout.html'), name = 'logout'),
    path('contact/', views.contact, name = 'contact'),
    path('conditions/', views.conditions, name = 'conditions'),
    path('mentions/', views.mentions, name = 'mentions'),
    path('donnees/', views.donnees, name = 'donnees'),
]
