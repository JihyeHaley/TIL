from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 3)

    page_num = request.GET.get('page')
    articles = paginator.get_page(page_num)

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)


def create(request):
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form' : form,
    }

    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # form = ArticleForm(instance=article)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context )


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')