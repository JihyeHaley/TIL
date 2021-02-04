'''
    레벤슈타인 거리 계산하기
'''

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


# 완전히 동일
def _check_totally_same(a, b):
    if a == b:
        return True


# 대문자화 동일한지 확인
def _check_upper_same(a, b):
    if a == b:
        return True


# 유사도 측정하기 : 레벤슈타인 거리 계산하기
def _calc_distance(a, b):
    # 대문자화해서 같음을 확인하기
    if _check_totally_same(a, b) == True or _check_upper_same (a, b) == True: 
        return 0

    a_len = len(a)
    b_len = len(b)
    if a == '' : 
        return b_len 
    if b == '' : 
        return a_len

    #2차원 배열(a_len+1, b_len+1)준비하기 --(#1)
    matrix= [[]for i in range(a_len + 1)] #a길이+1 만큼의 크기의 배열준비
    for i in range(a_len+1) :
        matrix[i] = [0 for j in range(b_len + 1)] #0으로 초기화(2차원배열)    
   
    #0일때 초기값을 설정 (#2)
    for i in range(a_len + 1):
        matrix[i][0] = i   
    for j in range(b_len + 1):
        matrix[0][j] = j
    
    #표 채우기 --(#3)
    for i in range(1, a_len + 1):
        ac=a[i-1]  #a의 첫번째 글자(=[0]) 부터 시작
        for j in range(1, b_len + 1):
            bc=b[j-1] #b의 첫번째글자(=[0]) 부터 시작
            # cost=0 if (ac == bc) else 1 #a[i-1]과 b[j-1] 이 같다면 비용(cost)은 0. 같지 않으면 1
            if ac == bc:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min([  #min 함수 : 최소값을 돌려줌; 
            #a의 i번째까지의 문자와 b의 j번째까지의 문자를 비교해서, 삽입/제거/변경 비용 중 최소값으로 표를 채운다.
                matrix[i - 1][j] + 1,     # 문자 삽입
                matrix[i][j - 1] + 1,     # 문자 제거
                matrix[i - 1][j - 1] + cost # 문자 변경
            ])
    return matrix[a_len][b_len] #최종적으로는, 표의 오른쪽 아래에 있는 값이 최소거리(레벤슈타인 거리)가 된다.
    #ㄴ함수 calc_distance 끝


# 유사도 측정
def _check_similarity(google_sent, papago_sent):
    similarity_price = list()
    #실행 예
    samples = [google_sent, papago_sent]
    base = samples[0] # 구글 중심
    r = sorted(samples, key = lambda n: _calc_distance(base, n)) #base(신촌역)과 samples의 각 원소 비교
    for n in r:
        similarity_price.append(_calc_distance(base, n))
        # print(calc_distance(base, n), n)
    return similarity_price