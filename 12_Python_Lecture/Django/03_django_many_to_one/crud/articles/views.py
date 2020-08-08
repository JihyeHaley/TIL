from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: 
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index') 

@require_POST
# POST방식으로밖에 없을 거니깐 if/else를 쓰지말고...
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    # contents = request.POST.get('contents')
    # Comment.objects.create(article=article, contents=contents)
    
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False) 
        # create함수 쓰기 전에 save 를 하기 전에 
        # 객체는 만들어져 있지만 반영이 안되어있는 상태, 객체만 만들어줘 (임시저장)
        comment.article = article
        comment.save()

    return redirect('articles:detail', article.pk)


@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('articles:detail', article_pk)
