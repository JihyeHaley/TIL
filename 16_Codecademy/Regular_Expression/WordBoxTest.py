import re
# print('---------------------비캡쳐-----------------------')
# print('using.... (?:<regex>)')
# matchObj = re.search('((?:ab)+), ((?:123)+) is repetitive\.', 'Hmm... ababab, 123123 is repetitive.')
# print(matchObj.group(0))
# print(matchObj.group(1))
# print(matchObj.group(2))


a = '적대적  M&A를  일종의  시장  규율(market  discipline)로  보는  입장에서는  적대적  M&A에  대한방어는  불가하다고  본다.'
b = '혼성단체(hybrid  entity)혼성비대칭 거래(hybrid  mismatch  arrangements)구나 2018년 5월 베이징에서 열린 ISO/TC 184 연례회의(Super Meeting)에서는 스마트 제조가 주요 화제였다.'
c = '소뇌편도헤르니아(Cerebellar ton-sillar herniation)의 위험을 일으킬 수 있다.'
d = '본 환자의 경우, 보호자가 전신마취(general anesthesia)를 거부하여 신경외과 의사와 수술 및 마취 방법에 대하여 상의하였다.'
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
        
en_words, en_words_len = find_En(b)

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


ko_words = find_Ko(b, en_words_len)
for i in range(len(ko_words)):
    print(i+1, ko_words[i], en_words[i])



    

# def find_Korean(sent):
#     match, terminated = find_English(sent)
#     return_times = len(match)
#     print(return_times)
#     eng_at_least = '3,'
#     korean_sp_english_sp = f'((([ㄱ-ㅣ가-힣]+)\s?)\s?){return_times}(\s?\(?(([a-zA-Z]){eng_at_least}\s*){return_times}+\)?)'
#     match = re.findall(korean_sp_english_sp, sent)
#     return match

def find_pattern(sent):
    # rabbit = '((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'
    match = re.findall('((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)', sent)
    return match


rabbit = r'((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'