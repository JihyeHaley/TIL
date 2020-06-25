from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required 

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form' : form,
    }
    return render(request, 'posts/form.html', context)