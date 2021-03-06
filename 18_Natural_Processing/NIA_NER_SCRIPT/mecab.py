import MeCab
# from konlpy.tag import Mecab
import re
import xlsxwriter

## excel idx 
def excel_index_creator(colum, row_idx):
    colum_idx = colum + str(row_idx)
    return colum_idx



#  후보군 1. 한글과 영어 둘다 있어? (10초 빠름)
def isSentKoreanAndEnglish(sent):
    ko_en = re.compile('.*[a-zA-Z]+')
    # ko_en = re.compile('.*[ㄱ-ㅣ가-힣]+\(.*[a-zA-Z]+\)')
    # return bool(ko.fullmatch(text))
    return bool(ko_en.match(sent))



#  후보군 2. 괄호가 있어? 
def isSentHasSSC(sent):
    ssc = re.compile('.*\(.*\)+')
    # return bool(ko.fullmatch(text))
    return bool(ssc.match(sent))



# 형태소 분석
def start_mecab(sent):
    m = MeCab.Tagger()
    te = m.parse(sent)
    return te
    # tagger = Mecab()
    # print(tagger.pos('혼성단체(hybrid  entity)혼성비대칭 거래(hybrid  mismatch  arrangements)구나 2018년 5월 베이징에서 열린 ISO/TC 184 연례회의(Super Meeting)에서는 스마트 제조가 주요 화제였다.'))



#  단어, 품사 구별 [짝수(단어), 품사[0](품사)]
def words_morph(sent):
    # mecab = Mecab()
    # sent = 'u'+sent
    # sent = mecab.pos('u'+sent)
    sent = re.sub(r'(\,\*)*(\n|\t)','\n', sent)
    sent = sent.split('\n')
    return sent



# 품사를 모두 모아서 String으로 만들어주기 (pattern을 잡기위해서)
# raw_mor 한 문장을 쪼개서 짝수 - 단어, 홀수 - 형태
def split_words_collect_mors(raw_mor):
    key = ''
    value = ''
    word_mor_dict = dict()
    words_list = list()
    words_one_str = str()
    morphemes_list = list()
    morphemes_one_str = str()
    for i in range(len(raw_mor)):
        # words_list.append(raw_mor[i][0])
        # morphemes_list.append(raw_mor[i][1])
        # morphemes_one_str += raw_mor[i][1]
        # print(i+1)
        # 짝수
        if i % 2 == 0:
            key = raw_mor[i]
            # print(key)
            words_list.append(key)
            words_one_str += key
        # 홀수
        else: 
            # wecab으로 뽑아낸 형태소의 값 1개만 뽑아주기 위해서
            value = raw_mor[i].split(',')
            value = value[0]
            # print(value)
            morphemes_list.append(value)
            morphemes_one_str += value
        
        word_mor_dict[key] = value


    return words_list, morphemes_list, morphemes_one_str




# 패턴찾아서 형태소 리스트 만들기
# 품사를 모두 모아서 String으로 만들어주기 (pattern을 잡기위해서)
def find_mor_pattern(morphemes_one_str):
    # mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    # mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)' #괄호 있어야만함
    # mor_pattern = '(XPN|XSV)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    # mor_pattern = '(XPN|XSV)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)'#괄호 있어야만함
    # mor_pattern = '(VV\+ETM)?(MM)?(XPN|XSV)?(ETN)?(NNG|NNP)(XSN|XSV|XSA)?(JX)?(XPN|XSV)?(ETN)?(NNB)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(NNG|NNP)?(XSN|XSV|XSA)?(JKO)?(SSO)(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SY)?(SL)?(SL)?(SC)?(SL)?'#괄호 있어야만함
    mor_pattern = '(VV\+ETM)?(MM)?(XPN|XSV)?(ETN)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(NNB)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(NNG|NNP)?(XSN|XSV|XSA)?(JKO)?(SSO)(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SY)?(SL)?(SL)?(SC)?(SL)?'#괄호 있어야만함
    
    mor_match_pre = re.findall(mor_pattern, morphemes_one_str, flags=0)
    mor_match_list= list()
    # ''없애주기 
		# 캡처하지 못한 아이들은 버리기 len(i) >= 1 로 해서
    for i in range(len(mor_match_pre)):
        sample = [i for i in mor_match_pre[i] if len(i) >= 1 ]
        mor_match_list.append(sample)
    # print('mor_match_list:', mor_match_list)
    return mor_match_list


# 영어(한글) 형식을 찾아보기 - 필요하면 사용할것. 이 파일에서는 현재 사용되지 않음
def find_isEnglishNKorean(morphemes_one_str):
    sep_mor_pattern = '(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SY)?(SL)?(SL)?(SC)?(SL)?(SSO)(VV\+ETM)?(MM)?(XPN|XSV)?(ETN)?(NNG|NNP)(XSN|XSV|XSA)?(JX)?(XPN|XSV)?(ETN)?(NNB)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(NNG|NNP)?(XSN|XSV|XSA)?(JKO)?(SSC)'#괄호 있어야만함
    sep_match_pre = re.findall(sep_mor_pattern, morphemes_one_str, flags=0)
    sep_mor_match_list= list()
    # ''없애주기 ㄴ
		# 캡처하지 못한 아이들은 버리기 len(i) >= 1 로 해서
    for i in range(len(sep_match_pre)):
        sample = [i for i in sep_match_pre[i] if len(i) >= 1 ]
        sep_mor_match_list.append(sample)
    # print('mor_match_list:', mor_match_list)
    return bool(sep_mor_match_list)



# 형태소 패턴 (list)와 일치하는 단어(list) 찾아서 추출
# morphemes_list는 words_list의 idx를 구하기 위해서
def find_word(mor_match_list, words_list, morphemes_list):
    word_match_list = list()
    for mor_match_idx in range(len(mor_match_list)):
        
        for i in range(0, len(morphemes_list)-len(mor_match_list[mor_match_idx])):
            comparison = [morphemes_list[j] for j in range(i, i+len(mor_match_list[mor_match_idx]))]
           
            if comparison == mor_match_list[mor_match_idx]:
                
                word_match_list.append(words_list[i:i+len(mor_match_list[mor_match_idx])])
                
    # print('word_match_list:', word_match_list)
    return word_match_list, mor_match_list


# 단어 만들기 완성판
def find_pattern_show_words(sent):
    # 형태소 분석
    te = start_mecab(sent)


    # 단어, 품사 구별 [짝수(단어), 품사[0](품사)
    raw_mor = words_morph(te)
    
    
    # dict_list에 구별해서 단어, 형태소 각각 넣어주기
		# raw_mor 한 문장을 쪼개서 짝수 - 단어, 홀수 - 형태
		# 품사를 모두 모아서 String으로 만들어주기 (pattern을 잡기위해서)
    words_list, morphemes_list, morphemes_one_str = split_words_collect_mors(raw_mor)


    # 패턴찾아서 형태소 리스트 만들기
    mor_match_list = find_mor_pattern(morphemes_one_str)
    # if find_isEnglishNKorean(morphemes_one_str) == True:
    #     print('영어(한글) 있어요')
    #     eng_kor += 1
    # print(mor_match_list)
    # 형태소 패턴 (list)와 일치하는 단어(list) 찾아서 추출
    word_match_list, mor_match_list = find_word(mor_match_list, words_list, morphemes_list)
    
	# Raw Sent에 대한 수술 후 뽑혀진 한-영 짝꿍들
    ko_words, en_words = make_word_str(word_match_list)

    mor_match_list_str = connect_listed_str_to_one(mor_match_list)

    return te, ko_words, en_words, mor_match_list_str


    
# 한글입니까?
def isKorean(single_word):
    ko = re.compile('[ㄱ-ㅣ가-힣]')
    return bool(ko.match(single_word))



# 영어입니까?
def isEnglish(single_word):
    en = re.compile('[a-zA-Z]')
    return bool(en.match(single_word))




# 살릴 단어 만들기
def make_word_str(word_matched_list):
    ko_words = list()
    en_words = list()
    for single_list in word_matched_list:
        # print(single_list)
        ko_word = str()
        en_word = str()
        for single_word in single_list:
            # 한글 만들어주기
            if isKorean(single_word) == True:
                if single_word in ['은', '는', '을', '를', '이', '가', '경우', '의한']:
                    continue
                ko_word += single_word + ' '
            # 영어 만들어주기
            elif isEnglish(single_word) == True:
                en_word += single_word + ' '
        ko_words.append(ko_word[:-1])
        en_words.append(en_word[:-1])
        # print(ko_words, '-', en_words)
    return ko_words, en_words



# 어떤 패턴으로 뽑혔는지 확인하기 위해서
def connect_listed_str_to_one(mor_match_list):
    # 어떤 패턴으로 뽑혔는지 확인하기 위해서
    mor_match_list_str = list()
    for mm in mor_match_list:
        mmp = ''
        for m in range(len(mm)):
            if m == len(mm):  
                mmp += mm[m]
            mmp += mm[m] + '-'
        mor_match_list_str.append(mmp[:-1])
    return mor_match_list_str


def skip_mored_word(mored_word):
    skip_word = ['a', 'aa', 'aaa', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vv', 'vii', 'viii', 'x', 'xx', 'ix', 'xi', 'xiv', 'xiii', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VV', 'VII', 'VIII', 'X', 'XX', 'IX', 'XIII']
    if len(mored_word) == 1 or mored_word in skip_word:
        return True
    else:
        return False
        

