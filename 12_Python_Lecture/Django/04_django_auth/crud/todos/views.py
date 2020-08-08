from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    # index에서 입력받으니깐
    form = TodoForm()
    #todos = Todo.objects.all()
    context = {
        'form' : form,
        #'todos' : todos,
    }
    return render(request, 'todos/index.html', context)


@login_required
def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        # User 정보를 지금 가져올 수는 없다. 
        # 로그인한 사용자의 정보를 가져오는 것이 필요
        todo = form.save(commit=False)
        # User 정보를 가져와야지
        todo.user = request.user
        todo.save()
        return redirect('todos:index')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')


    
    