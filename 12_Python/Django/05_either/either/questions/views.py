from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods,  require_POST
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


# Create your views here.
def index(request):
    return render(request, 'questions/index.html')

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions:detail', question.pk)
    else:
        form = QuestionForm()
        
    context = {
        'form': form,
    }   
    
    return render(request, 'questions/form.html', context)


def detail(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
    # if question_pk값이 삭제된거라면 404 에러가 나는게 가장 좋다. 
    # (바로 아래 get_object_or_404()참고)
    # 기능은 --> if pk 값이 유효하지 않는걸 요청 받았을때 404에러를 발생시킨다.

    question = get_object_or_404(Question, pk=question_pk)
    answers = question.answer_set.all()
    # 답이 다 다르니깐, fitler를 적용시켜서 답 갯수 세기 전 작업을 한다.
    # or, answer.filter(choice='a').count()
    answer_a = len(answers.filter(choice='a'))
    answer_b = len(answers.filter(choice='b'))
    total = answer_a + answer_b
    
    if total == 0:
        width_a = 0
        width_b = 0
    else:
        width_a = round(answer_a / total * 100, 1)
        width_b = round(answer_b / total * 100, 1)
    answer = AnswerForm()
    context = {
        'answer_a' : answer_a,
        'answer_b' : answer_b,
        'width_a' : width_a,
        'width_b' : width_b,
        'total' : total,
        'question' : question,
        'answer' : answer,
    }
    return render(request, 'questions/detail.html', context)

@require_POST
def answer_create(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        # get_objects_or_404 documentation 다시보기
        answer.question = question
        answer.save()
        return redirect('questions:detail', question_pk)
