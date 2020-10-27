import re
# from nltk.tokenize import LineTokenizer, Spacetokenizer, TweetTokenizer
# from nltk import word_tokenize

# # 영어 단어, 덩어리 개수 count 
# def count_En_words(match):
#     en_words_len = list()
#     en_words = list()

#     for i in match:
#         en_words.append(i[0]) # 살릴 단어
#         en_words_len_pre = i[0].split(' ') # 단어 덩어리 개수 
#         cnt = 0
#         for j in en_words_len_pre:
#             if j == '' or j == '  ':
#                 continue
#             cnt += 1
#         en_words_len.append(cnt)
#     return en_words_len, en_words



# # 영어 단어, 덩어리 개수 count 
# def count_Ko_words(match):
#     ko_words = list()
#     for i in match:
#         ko_words.append(i[0]) # 살릴 단어
#     return ko_words


# # 한글입니까?
# def isKorean(single_word):
#     ko = re.compile('[ㄱ-ㅣ가-힣]')
#     return bool(ko.match(single_word))



# # 영어입니까?
# def isEnglish(single_word):
#     en = re.compile('[a-zA-Z]')
#     return bool(en.match(single_word))



# 영어 단어 찾기 (각 영어 단어의 덩어리 길이 저장)
def find_En(sent):
    # en_pattern = re.compile('(\s?\(?(([a-zA-Z]){3,}\s*)+\)?)')
    en_words_pre = re.findall(r'(\(){1}([a-zA-Z])*(\)){1}', sent)
    en_words = str()
    print(en_words_pre)
    for ewp in en_words_pre:
        # if isEnglish(ewp) == True:
        en_words += ewp
    return en_words
        

def find_Ko(sent):
    # print(en_words_len)
    ko_words_pre = re.findall(r'([ㄱ-ㅣ가-힣]+)(\s)?(\(){1}(([a-zA-Z])\s)*(\)){1}', sent)
    ko_words = str()
    for kwp in ko_words_pre:
        # if isKorean(kwp) == True:
        ko_words += kwp
    return ko_words
    # ko_words = list()
    # for kwp in ko_words_pre:
    #     ko_word_pre = str()
    #     for _ in kwp:
    #         if isKorean(_) == True:
    #             ko_word_pre += _
    #     ko_words.append(ko_word_pre)
    # return ko_words




  


# def find_pattern(sent):
#     # rabbit = '((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'
#     match = re.findall('((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z])\s*)\)?)', sent)
#     return match


rabbit = r'((([ㄱ-ㅣ가-힣]+)\s?)\s?){2}(\s?\(?(([a-zA-Z]){3,}\s*)\)?)'