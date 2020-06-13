# django import style guide
# 1. standard library 최상단에 
# 2. 3rd party library
# 3. django
# 4. local django

import random
import requests
from pprint import pprint
from datetime import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    foods = ['샐러드', '타코', '딤섬', '쌀국수'] 
    pick = random.choice(foods)
    context = {
        'pick' : pick,
    }
    return render(request, 'articles/dinner.html', context)
    #딕셔너리 형태로 보내게 된다.


def randomImg(request):
    picked_Img = 'https://picsum.photos/200/300.jpg'
    randoms = ["wow", "sugoi", "haohao"]
    random_comment = random.choice(randoms)
    context = {
        'picked_Img' : picked_Img,
        'random_comment' : random_comment,
    }
    return render(request, 'articles/randomImg.html', context)


def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)


def introMe(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'articles/introMe.html', context)


def calculation(request, num1, num2) :
    result = num1 * num2 
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result,
    }
    return render(request, 'articles/calculation.html', context)


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
    return render(request, 'articles/dtl_practice.html', context)


def rotator(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {
        'word' : word,
        'result' : result,
    }
    return render(request, 'articles/rotator.html', context)


def throw(request):
    #페이지만 보여주면 되니깐, return renter만 하면 된다.
    return render(request, 'articles/throw.html') 


def catch(request):
    #사용자가 보낸 정보는 request안에 있다.
    # [] -> error 발생
    print(request.GET['message']) 
    # .get('') none 값으로 나옴. server안멈춤
    print(request.GET.get('hi')) 
    pprint(request.META)
    message = request.GET.get('message')
    name = request.GET.get('name')
    contenxt = {
        'message' : message,
        'name' : name,
    }
    return render(request, 'articles/catch.html', contenxt)


def lotto_throw(request):
    return render(request, 'articles/lotto_throw.html')


def lotto_catch(request):
    name = request.GET.get('name')
    randoms = range(1,46)
    lotto = sorted(random.sample(randoms, 6))
    #lotto = random.sample(randoms,6).sort() 는 리턴값이 없다.
    content = {
        'name' : name,
        'lotto' : lotto,
    }
    return render(request, 'articles/lotto_catch.html', content)


def artii(request):
    #fonts_list를 여기서 추출해줘야지 요청 페이지에서 볼 수 있다.
    #1. font URL
    font_URL = 'http://artii.herokuapp.com/fonts_list'

    # 2. ARTII api fontlist로 요청을 보내 폰트 정보를 받는다.
    font_response = requests.get(font_URL).text
    #print(type(font_response))

    # 3. 문자열 데이터를 리스트로 변환한다.
    # enter로 문자열들이 구분되어 이썽서 split함수를 사용해서 list로 만들어 주는 과정
    fonts_list = font_response.split('\n')
    #print(fonts_list)
    
    context = {
        'fonts_list' : fonts_list,
    }
    return render(request, 'articles/artii.html', context)


def artii_result(request):
    # 1. form에서 넘어온 데이터를 받는다. (word, font를 artii에서 받아야 한다.)
    word = request.GET.get('word')
    font = request.GET.get('font')

    # 2. 선택해서 보여주기
    ARTII_URL = f'http://artii.herokuapp.com/make?text={word}+art&font={font}'
    
    print('word :' + word)
    print('font :' + font)
    # 3. artii api주소로 우리가 만든 데이터와 함께 요청을 보낸다.
    result = requests.get(ARTII_URL).text
    context = {
        'result' : result,
    }

    return render(request, 'articles/artii_result.html', context)