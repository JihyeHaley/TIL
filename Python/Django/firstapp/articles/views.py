# django import style guide
# 1. standard library 최상단에 
# 2. 3rd party library
# 3. django
# 4. local django

import random
from datetime import datetime
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


def randomImg(request):
    picked_Img = 'https://picsum.photos/200/300.jpg'
    randoms = ["wow", "sugoi", "haohao"]
    random_comment = random.choice(randoms)
    context = {
        'picked_Img' : picked_Img,
        'random_comment' : random_comment,
    }
    return render(request, 'randomImg.html', context)


def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)

def introMe(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'introMe.html', context)


def calculation(request, num1, num2) :
    result = num1 * num2 
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result,
    }
    return render(request, 'calculation.html', context)


def dtl_practice(request):
    foods = ['타코', '브리또', '오뎅', '딤섬']
    empty_list = []
    messages = 'Life is hosrt, you need Python...'
    datetime_now = datetime.now()
    context = {
        'foods' : foods,
        'empty_ist' : empty_list,
        'messages' : messages,
        'datetime_now' : datetime_now,
    }
    return render(request, 'dtl_practice.html', context)

def rotator(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {
        'word' : word,
        'result' : result,
    }
    return render(request, 'rotator.html', context)