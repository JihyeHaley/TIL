from django.shortcuts import render, redirect
from .models import Movies
from .forms import MoviesForm


# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MoviesForm()
    context = {
        'form' : form,
    }

    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movies.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)