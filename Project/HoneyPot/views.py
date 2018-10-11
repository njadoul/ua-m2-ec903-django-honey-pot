from django.shortcuts import render, redirect
from django.contib.auth import login, authenticate
from Project.core.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profil.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, username)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})
