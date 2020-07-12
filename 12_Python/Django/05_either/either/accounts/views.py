from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def signup(request):
    # if 사용자가 로그인 했으면 login으로 보내줘
    if request.user.is_authenticated:
        return redirect('questions:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('questions:index')
    # 1번 단계
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
    return redirect('accounts:login')



