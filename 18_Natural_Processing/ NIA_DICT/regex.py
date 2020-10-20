import re
# from nltk.tokenize import LineTokenizer, Spacetokenizer, TweetTokenizer
# from nltk import word_tokenize

# 영어 단어, 덩어리 개수 count 
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


# 영어 단어 찾기 (각 영어 단어의 덩어리 길이 저장)
def find_En(sent):
    # en_pattern = re.compile('(\s?\(?(([a-zA-Z]){3,}\s*)+\)?)')
    allMatch = re.findall(r'(\s?\(?(([a-zA-Z]){3,}\s*)+\)?)', sent)

    # 영어 단어, 덩어리 개수 count 함수 호출
    en_words_len, en_words = count_En_words(allMatch)
    
    return en_words, en_words_len
        

# 영어 단어, 덩어리 개수 count 
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



def find_pattern(sent):
    # rabbit = '((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'
    match = re.findall('((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z])\s*)\)?)', sent)
    return match


rabbit = r'((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'