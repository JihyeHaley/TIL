from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
#GET, POST가 아니면 모두 405 error를 내보내준다.
def create(request):
    # POST 일 때
    if request.method == 'POST' :
    # 전체를 한번에 다 받아준다.
        form = ArticleForm(request.POST) # 데이터 베이스 조작 = POST
        # 서버가 이용할 때 데이터를 조작할 걸 알기때문에 POST만 분류
        # 유효성 검사, 통과하면 저장, 통과 못하면 어딘가로 되돌려 보낸다.
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    
    # POST가 아닌 다른 methods일 때
    else: # POST 가 아닌 다른 method 전부가 있기 때문에
        form = ArticleForm()

    
    context = {
        # form의 두가지 모습
        # 1. is_valid()에서 통과하지 못한 form일 경우와(error message포함)
        # 2. else 구문의 form
        'form' : form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# GET = 수정을 위한 페이지
# POST  = 실제 변조

@require_http_methods(['GET', 'POST'])
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect ('articles:detail', article.pk)
    else: #아직받아온 것이 없어서 꼭 else를 먼저 만들기
        form = ArticleForm(instance=article)
    
    
    context  = {
        'form' : form,
    }

    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

    
