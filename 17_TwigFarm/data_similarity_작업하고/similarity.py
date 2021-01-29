import math

import numpy as np
from nltk.util import ngrams
from similarity_utils import _check_totally_same, _check_upper_same
from tensorflow.keras.preprocessing.text import text_to_word_sequence
# from sklearn.feature_extraction.text import TfidfVectorizer

a = 'There is a habit of looking for only good things more than enough.'
b = 'I have a habit of finding only good things that are more than just enough.'


def calc_distance(a,b):
    '''레벤슈타인 거리 계산하기'''
    
    # 동일하면 바로 유사도 0 (제일 정확도가 높다는 뜻)
    if _check_totally_same(a, b) == True or _check_upper_same (a, b) == True: 
        return 0

    a_len=len(a)
    b_len=len(b)
    if a == '' : 
        return b_len 
    if b == '' : 
        return a_len

    #2차원 배열(a_len+1, b_len+1)준비하기 --(#1)
    matrix= [[] for i in range(a_len + 1)] #a길이+1 만큼의 크기의 배열준비
    for i in range(a_len+1) :
        matrix[i] = [0 for j in range(b_len+1)] #0으로 초기화(2차원배열)    
   
    #0일때 초기값을 설정 (#2)
    for i in range(a_len+1):
        matrix[i][0]=i   
    for j in range(b_len+1):
        matrix[0][j]=j
    
    #표 채우기 --(#3)
    for i in range(1,a_len+1):
        ac=a[i - 1]  #a의 첫번째 글자(=[0]) 부터 시작
        for j in range(1, b_len + 1):
            bc=b[j - 1] #b의 첫번째글자(=[0]) 부터 시작
            #a[i-1]과 b[j-1] 이 같다면 비용(cost)은 0. 같지 않으면 1
            if ac == bc:
                cost = 0
            else:
                cost = 1
            cost=0 if (ac ==bc) else 1 
            matrix[i][j] = min([  #min 함수 : 최소값을 돌려줌; 
            #a의 i번째까지의 문자와 b의 j번째까지의 문자를 비교해서, 삽입/제거/변경 비용 중 최소값으로 표를 채운다.
                matrix[i-1][j] + 1,     # 문자 삽입
                matrix[i][j-1] + 1,     # 문자 제거
                matrix[i-1][j-1] + cost # 문자 변경
            ])
    return matrix[a_len][b_len] #최종적으로는, 표의 오른쪽 아래에 있는 값이 최소거리(레벤슈타인 거리)가 된다.
    #ㄴ함수 calc_distance 끝


def tokenized_calc_distance(a,b):
    '''레벤슈타인 거리 계산하기'''
    sa_list = text_to_word_sequence(a)
    sb_list = text_to_word_sequence(b)
    # 동일하면 바로 유사도 0 (제일 정확도가 높다는 뜻)
    if _check_totally_same(a, b) == True or _check_upper_same (a, b) == True: 
        return 0

    a_len=len(sa_list)
    b_len=len(sb_list)
    if a == '' : 
        return b_len 
    if b == '' : 
        return a_len

    #2차원 배열(a_len+1, b_len+1)준비하기 --(#1)
    matrix= [[] for i in range(a_len + 1)] #a길이+1 만큼의 크기의 배열준비
    for i in range(a_len+1) :
        matrix[i] = [0 for j in range(b_len+1)] #0으로 초기화(2차원배열)    
   
    #0일때 초기값을 설정 (#2)
    for i in range(a_len+1):
        matrix[i][0]=i   
    for j in range(b_len+1):
        matrix[0][j]=j
    
    #표 채우기 --(#3)
    for i in range(1,a_len+1):
        ac=sa_list[i - 1]  #a의 첫번째 글자(=[0]) 부터 시작
        for j in range(1, b_len + 1):
            bc=sb_list[j - 1] #b의 첫번째글자(=[0]) 부터 시작
            #a[i-1]과 b[j-1] 이 같다면 비용(cost)은 0. 같지 않으면 1
            if ac == bc:
                cost = 0
            else:
                cost = 1
            cost=0 if (ac ==bc) else 1 
            matrix[i][j] = min([  #min 함수 : 최소값을 돌려줌; 
            #a의 i번째까지의 문자와 b의 j번째까지의 문자를 비교해서, 삽입/제거/변경 비용 중 최소값으로 표를 채운다.
                matrix[i-1][j] + 1,     # 문자 삽입
                matrix[i][j-1] + 1,     # 문자 제거
                matrix[i-1][j-1] + cost # 문자 변경
            ])
    return matrix[a_len][b_len] #최종적으로는, 표의 오른쪽 아래에 있는 값이 최소거리(레벤슈타인 거리)가 된다.
    #ㄴ함수 calc_distance 끝



# 문장을 넣어서 유사도 알기
def ngram(sent, num):
    res = []
    slen = len(sent) - num + 1
    for i in range(slen):
        ss = sent[i:i+num]
        res.append(sent)
    return res


# ngram으로 유사도  측정하기 (2개씩)[토큰]
def diff_ngram(idx, sa, sb, num):
    sb_list = text_to_word_sequence(sa[idx])
    sb_list = text_to_word_sequence(sb[idx])
    a = ngram(sb_list, num)
    b = ngram(sb_list, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    print(cnt)
    print(len(a))
    lenght = int()
    if len(a) == 0:
        lenght = 1
    else:
        lenght = len(a)
    return cnt / lenght


a = ["오늘 강남에서 맛있는 스파게티를 먹었다."]
b = ["강남에서 먹었던 오늘의 스파게티는 맛있었다."]

# 2-gram
r2 = diff_ngram(0, a, b, 2)
print("2-gram:", r2)

