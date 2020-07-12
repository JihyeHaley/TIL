from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index.html')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')

    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')