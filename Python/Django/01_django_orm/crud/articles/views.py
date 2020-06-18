from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 1. new에서 보낸 데이터 받기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. DB에 저장
    # (2) 인스턴스 사용
    article = Article(title=title, content=content)
    # 데이터가 유효한지 검사
    article.save()

    # 3. context에 보내주기
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    print(request.method)
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' : 
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
    


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }

    return render(request, 'articles/edit.html', context)


    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()

    # return redirect('articles:index')


def update(request, pk):
    # 1. 수정할 게시글 조회
    article = Article.objects.get(pk=pk)
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # 2. edit 에서 보낸 이미지를 받아서 기존값을 받기
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)