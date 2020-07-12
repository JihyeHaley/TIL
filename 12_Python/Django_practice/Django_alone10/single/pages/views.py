from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'pages/index.html', context)


def new(request):
    return render(request, 'pages/new.html')


def create(request):
    # new에서 데이터값받기
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('pages:detail', article.pk)
    

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'pages/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    pk = article.pk
    context = {
        'pk' : pk,
    }
    
    if request.method == 'POST':
        article.delete()
        return render(request, 'pages/delete.html', context)
    else:
        return redirect('pages:detail', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'pages/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content =  request.POST.get('content')
    article.save()

    return redirect('pages:detail', article.pk)