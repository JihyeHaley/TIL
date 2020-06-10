# django import style guide
# 1. standard library 최상단에 
# 2. 3rd party library
# 3. django
# 4. local django

import random
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def dinner(request):
    foods = ['샐러드', '타코', '딤섬', '쌀국수'] 
    pick = random.choice(foods)
    context = {
        'pick' : pick,
    }
    return render(request, 'dinner.html', context)
    #딕셔너리 형태로 보내게 된다.