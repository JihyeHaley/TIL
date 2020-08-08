from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    # session이 유효하면, 로그인 할 필요 없으니깐 :) 
    if request.user.is_authenticated:
        return redirect('questions:index')

    # signup 할려고 button누른 후 생길 일들
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('questions:index')

    # signup을 해야하는 사람들
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/form.html', context)

 
def login(request):
    if request.user.is_authenticated:
        return redirect('questions:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            form.save()
            user = form.get_user()
            auth_login(request, user)
            return redirect('questions:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('questions:index')