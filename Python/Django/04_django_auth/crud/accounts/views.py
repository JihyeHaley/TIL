from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # model에 save가 맞다.
            return redirect('account:login')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        # 구조가 UserCreationForm하고는 다르다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save()가 아니다. / login 함수를 갖다 쓰면된다.
            auth_login(request, form.get_user())
            # login 함수는 -> login(1번째이자-request, 2번째인자-user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
