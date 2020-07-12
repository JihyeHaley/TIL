from pprint import pprint
from django.shortcuts import render


# Create your views here.
def index(request, name, age):
    content = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'articles/index.html', content)


def form_practice_a(request):
    return render(request, 'articles/form_practice_a.html')


def form_practice_b(request):
    
    name = request.GET.get('name')
    age = request.GET.get('age')
    message = request.GET.get('message')

    content = {
        'message' : message,
        'name' : name,
    }
    content = {
        'name' : name,
        'age' : age,
        'message' : message,
    }
    return render(request, 'articles/form_practice_b.html', content)
