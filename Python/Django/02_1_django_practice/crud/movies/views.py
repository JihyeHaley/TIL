from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    
    else:
        form = MovieForm()

    context = {
        'form' : form,
    }

    return render(request ,'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    title = movie.title
    context = {
        'title' : title,
    }
    movie.delete()
    return render(request, 'movies/delete.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST' :
        form = MovieForm(request.POST, instance=movie)
        # 목적보어, 목적어
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else :
        form = MovieForm(instance=movie)
        #1. 데이터 받고
        #2. 저장 (기존의 정보가 이거야)
   
    context = {
        'form' : form,
    }

    return render(request, 'movies/update.html', context)


