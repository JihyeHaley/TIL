from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def user_ranking():
    User = get_user_model()
    users = User.objects.all()
    if len(users) >3:
        while len(users) == 3:
            del users[-1]
    
    ranking = {
        'ranking' : users,
    }
    # return User.objects.all()
    return ranking
    # rankings = user_ranking()


def signup(request):
    rankings = user_ranking()
    if request.user.is_authenticated :
        return redirect('foother-index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('maps:review-all')

    else:
        form = CustomUserCreationForm()
    
    context = {
        'form' : form,
        'rankings' : rankings
    }

    return render(request, 'accounts/form.html', context)


def login(request):
    rankings = user_ranking()
    if request.user.is_authenticated:
        return redirect('foother-index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # user = form.save()
            user = form.get_user()
            auth_login(request, user)
            return redirect('maps:review-all')

    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form,
        'rankings' : rankings,
    }

    return render(request, 'accounts/form.html', context)


@login_required
def detail(request, username):
    rankings = user_ranking()
    user = User.objects.get(username=username)

    context = {
        'user' : user,
        'rankings' : rankings,
    }
    return render(request, 'accounts/detail.html', context)


@login_required
def update(request, username):
    rankings = user_ranking()
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect ('accounts:profile', user.username)
    else:
        form = CustomUserCreationForm(instance=user)
    
    context = {
        'form' : form,
        'rankings' : rankings,
    }

    return render(request, 'accounts/update.html', context)


def logout(request):
    auth_logout(request)
    return redirect('foother-index')



def profile(request, username):
    rankings = user_ranking()
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), username=username)
        context = {
            'user_profile' : user,
            'rankings' : rankings,
        }
    else:
        return redirect('foother-index')
        
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, username):
    you = get_object_or_404(User, username=username)
    me = request.user
    if me != you:
        if you.followers.filter(username=me.username).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', you.username)