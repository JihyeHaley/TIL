import re
from eunjeon import Mecab
import MeCab
from konlpy.tag import Kkma
# print('---------------------비캡쳐-----------------------')
# print('using.... (?:<regex>)')
# matchObj = re.search('((?:ab)+), ((?:123)+) is repetitive\.', 'Hmm... ababab, 123123 is repetitive.')
# print(matchObj.group(0))
# print(matchObj.group(1))
# print(matchObj.group(2))


a = '적대적  M&A를  일종의  시장  규율(market  discipline)로  보는  입장에서는  적대적  M&A에  대한방어는  불가하다고  본다.'
b = '본 환자의 경우, 보호자가 전신마취(general anesthesia)를 거부하여 신경외과 의사와 수술 및 마취 방법에 대하여 상의하였다.'
c = '소뇌편도헤르니아(Cerebellar ton-sillar herniation)의 위험을 일으킬 수 있다.'
d = '본 환자의 경우, 보호자가 전신마취(general anesthesia)를 거부하여 신경외과 의사와 수술 및 마취 방법에 대하여 상의하였다.'
e = '간에서 일어나는 일차 대사작용(first-pass metabolism)과 뇌혈관 장벽(blood-brain barrier)을 모두 피할 수 있다.'
f = '하지만 요추 복강 단락술 수술을 하는 경우, 요추내 압력(Lumbar spinal canal pressure)이 급격히 증가할 수있다.'
g = '척추 수술과 같이 토니켓(tourniquet)을 사용할 수 없어 출혈을 조절할 수 없는 수술에 있어 출혈량이 증가할 경우 저혈량성 쇼크에 빠질 수 있다.'
tc = list()
tc.append(a)
tc.append(b)
tc.append(c)
tc.append(d)


# 0. 영어 단어, 덩어리 개수 count 
def count_En_words(match):
    en_words_len = list()
    en_words = list()

    for i in match:
        alive = re.sub(r'\(|\)', '',i[0])
        en_words.append(alive) # 살릴 단어
        en_words_len_pre = i[0].split(' ') # 단어 덩어리 개수 
        cnt = 0
        for j in en_words_len_pre:
            if j == '' or j == '  ':
                continue
            cnt += 1
        en_words_len.append(cnt)
    return en_words_len, en_words

# 1. 영어 단어 찾기 (각 영어 단어의 덩어리 길이 저장)
def find_En(sent):
    # en_pattern = re.compile('(\s?\(?(([a-zA-Z]){3,}\s*)+\)?)')
    allMatch = re.findall(r'(\s?\(?(([a-zA-Z]){3,}\s*)+\)?)', sent)

    # 영어 단어, 덩어리 개수 count 함수 호출
    en_words_len, en_words = count_En_words(allMatch)
    return en_words, en_words_len
        
en_words, en_words_len = find_En(e)

def count_Ko_words(match):
    ko_words = list()
    for i in match:
        ko_words.append(i[0]) # 살릴 단어
    return ko_words


def find_Ko(sent, en_words_len):
    # print(en_words_len)
    allMatch = re.findall('((([ㄱ-ㅣ가-힣]+)\s?)\s?)(\s?\(?(([a-zA-Z]){3,}\s*)+\)?)', sent)
    Ko_words = count_Ko_words(allMatch)
    return Ko_words


ko_words = find_Ko(e, en_words_len)
for i in range(len(ko_words)):
    print(i+1, ko_words[i], en_words[i])



def find_Korean(sent):
    match, terminated = find_English(sent)
    return_times = len(match)
    print(return_times)
    eng_at_least = '3,'
    korean_sp_english_sp = f'((([ㄱ-ㅣ가-힣]+)\s?)\s?){return_times}(\s?\(?(([a-zA-Z]){eng_at_least}\s*){return_times}+\)?)'
    match = re.findall(korean_sp_english_sp, sent)
    return match

def find_pattern(sent):
    # rabbit = '((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'
    match = re.findall('((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)', sent)
    return match


rabbit = r'((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'



# 형태소 분석
def start_mecab(sent):
    m = MeCab.Tagger()
    te = m.parse(sent)
    print(te)
    return te
    # tagger = Mecab()
    # print(tagger.pos('혼성단체(hybrid  entity)혼성비대칭 거래(hybrid  mismatch  arrangements)구나 2018년 5월 베이징에서 열린 ISO/TC 184 연례회의(Super Meeting)에서는 스마트 제조가 주요 화제였다.'))

# 단어, 품사 구별
def words_morph(b):
    b = re.sub(r'(\,\*)*(\n|\t)','\n', b)
    b = b.split('\n')
    return b


def checkwhether(b):
    # 형태소 분석
    b = start_mecab(b)
    abc = [b]
    print(abc)

    # 단어, 품사 구별
    b = words_morph(b)
    # print(b)

    d = dict()
    key = ''
    value = ''
    raw_words = list()
    raw_words_str = str()
    morphemes = list()
    morphemes_str = str()

    for i in range(len(b)):
        print(i+1)
        # 짝수
        if i % 2 == 0:
            key = b[i]
            print(key)
            raw_words.append(key)
            raw_words_str += key
        # 홀수
        else: 
            value = b[i].split(',')
            value = value[0]
            print(value)
            morphemes.append(value)
            morphemes_str += value
        print()
        d[key] = value
    print(d)
    print(raw_words_str)
    print(morphemes_str)
    pattern = '(NNG)?(NNG)?(NNG)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    seriously_pre = re.findall(pattern, morphemes_str, flags=0)
    count_dummy = len(seriously_pre)
    seriously = list()
    for i in range(count_dummy):
        sample = [i for i in seriously_pre[i] if len(i) >= 1 ]
        seriously.append(sample)
    print(seriously)
    
    
    for d_helper in range(len(seriously)):
        print(len(morphemes))
        print(len(seriously[d_helper]))
        for i in range(0, len(morphemes)-len(seriously[d_helper])):
            comparison = [morphemes[j] for j in range(i, i+len(seriously[d_helper]))]
            # print(comparison)
            if comparison == seriously[d_helper]:
                print(raw_words[i:i+len(seriously[d_helper])])

    return morphemes_str

morphes_str = checkwhether(g)

a = '적대적  M&A를  일종의  시장  규율(market  discipline)로  보는  입장에서는  적대적  M&A에  대한방어는  불가하다고  본다.'
b = '본 환자의 경우, 보호자가 전신마취(general anesthesia)를 거부하여 신경외과 의사와 수술 및 마취 방법에 대하여 상의하였다.'
c = '소뇌편도헤르니아(Cerebellar ton-sillar herniation)의 위험을 일으킬 수 있다.'
d = '본 환자의 경우, 보호자가 전신마취(general anesthesia)를 거부하여 신경외과 의사와 수술 및 마취 방법에 대하여 상의하였다.'
e = '간에서 일어나는 일차 대사작용(first-pass metabolism)과 뇌혈관 장벽(blood-brain barrier)을 모두 피할 수 있다.'
f = '하지만 요추 복강 단락술 수술을 하는 경우, 요추내 압력(Lumbar spinal canal pressure)이 급격히 증가할 수있다.'

# print(re.findall('(NNG)+(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?', morphes_str))  # 12
# print(re.findall('A(12)+B', 'A12312B')) # 12
# print(re.findall('A(12)+B', 'A121212B')) # 12
# print(re.findall('A(12)+B', 'A12121212B')) # 12 
# def count_sso_ssc()
    # sso = list() # (
    # ssc = list() # )
    # sso_idx = list()
    # ssc_idx = list()



    # 괄호의 개수
    # for key, value in d.items():
    #     # (
    #     if value == 'SSO':
    #         for idx in range(len(raw_words)):
    #             if key == raw_words[idx]:
    #                 sso_idx.append(idx)
        
    #     #)
    #     if value == 'SSC':
    #         for idx in range(len(morphemes)):
    #             if key == morphemes[idx]:
    #                 ssc_idx.append(idx)
    #         print(ssc)
    





# Kkma
# kkma = Kkma()

# def morph(input_data) : 
#     preprocessed = kkma.pos(input_data) 
#     print(preprocessed)

# morph(b)