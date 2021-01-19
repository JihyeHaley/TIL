import MeCab
from konlpy.tag import Mecab
import re
import xlsxwriter
import timeit
from datetime import datetime


# 형태소 분석
def start_mecab(sent):
    m = MeCab.Tagger()
    te = m.parse(sent)
    return te
    

#  단어, 품사 구별 [짝수(단어), 품사[0](품사)]
def words_morph(sent):
    mecab = Mecab()
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
            # meecab으로 뽑아낸 형태소의 값 1개만 뽑아주기 위해서
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
    mor_pattern = '(VV\+ETM)?(MM)?(XPN|XSV)?(ETN)?(NNG|NNP)?(NNG|NNP)?(XR)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN+JX)?(VX)?(ETN)?(NNB)?(NNG|NNP)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(JKG)?(NNG|NNP)?(VA+ETM)?(IO)?(NNG|NNP)(XSN|XSV|XSA)?(XSA+ETM)?(JKO)?(SSO)(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SY)?(SL)?(SL)?(SC)?(SL)?(SL)?(SN)?(SN)?(SC)?(SL)?(SC)?(SN)?(SL)?(SN)?(SL)?(SSC)'#괄호 있어야만함 처음에만    
    mor_match_pre = re.findall(mor_pattern, morphemes_one_str, flags=0)
    mor_match_list= list()
    # ''없애주기 
		# 캡처하지 못한 아이들은 버리기 len(i) >= 1 로 해서
    for i in range(len(mor_match_pre)):
        sample = [i for i in mor_match_pre[i] if len(i) >= 1 ]
        mor_match_list.append(sample)
    # print('mor_match_list:', mor_match_list)
    return mor_match_list


# 형태소 패턴 (list)와 일치하는 단어(list) 찾아서 추출
# morphemes_list는 words_list의 idx를 구하기 위해서
def find_word(mor_match_list, words_list, morphemes_list):
    word_match_list = list()
    for mor_match_idx in range(len(mor_match_list)):
        
        for i in range(0, len(morphemes_list)-len(mor_match_list[mor_match_idx])):
            comparison = [morphemes_list[j] for j in range(i, i+len(mor_match_list[mor_match_idx]))]
           
            if comparison == mor_match_list[mor_match_idx]:
                
                word_match_list.append(words_list[i:i+len(mor_match_list[mor_match_idx])])
                

    return word_match_list, mor_match_list


# 한글입니까?
def isKorean(single_word):
    ko = re.compile('[ㄱ-ㅣ가-힣]')
    return bool(ko.match(single_word))


# 영어입니까?
def isEnglish(single_word):
    en = re.compile('[a-zA-Z]')
    return bool(en.match(single_word))


# 숫자입니까?
def isNumber(single_word):
    en = re.compile('[0-9]')
    return bool(en.match(single_word))


def skip_mored_word(mored_word):
    skip_word = ['Fig','fig', 'Fig.','fig.', 'r . ', 'Table', 'a', 'aa', 'aaa', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vv', 'vii', 'viii', 'x', 'xx', 'ix', 'xi', 'xiv', 'xiii', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VV', 'VII', 'VIII', 'X', 'XX', 'IX', 'XIII']
    if len(mored_word) <= 2 or mored_word in skip_word:
        return True
    else:
        return False  


# Fig 같이 필요 없는 덩어리 아예 없애기
def skip_dirty_words(mored_word):
    if 'see Fig' in mored_word  or 'Fig' in mored_word or 'r . ' in mored_word or 'Table' in mored_word:
        return True
    else:
        return False


# 제대로된 영어 찾아주기
def find_good_korean_english(word_match_list, sent):
    # 1차적 단어 모아주기
    en_words_pre = list()
    ko_words_pre = list()

    # 2차적 반복되는 단어 지워서 모아주기
    en_words = list()
    ko_words = list()
    # 형태소 분석으로 모은 단어들 <- 굉장히 너저분 한 세트 씩 가져오기 (한 문장에 2개 이상인 경우도 있어서 for문으로 돌려서 체크)
    for word_match in word_match_list:
        en_word = str() # 온전한 영어 단어 
        en_sample = str() # [(영어]
        sso_idx = 0 # '(' 가 리스틑에서 몇 번째 있는지,  용도=. word_match 에서 뒤에서 영어 단어 하나 가져와서 붙여서 그 앞(한글) 뒤(영어) 탐색할려고! 
        ssc = '' # 끝 괄호의 종류 체크----- ssc = ')' <- 형태소에서 인식하는 형태 
        btw_ko_en = 0 # sent안에서 [(영어] 시작이 어딘 idx인지 볼려고, 그거 찾아서 한글 탐색 할려고
        
        # 영어 먼저잡고 한글 잡자
        for chunk_idx, chunk in enumerate(word_match):
            # 괄호의 형태 찾기
            if chunk in ['(', '{', '[']:
                if chunk == '(':
                    ssc = ')'
                elif chunk == '{':
                    ssc = '}'
                elif chunk == '[':
                    ssc = ']'
                # 괄호 + 영어 한 단어  <- ex. ['재난', '관리', '(', 'disaster', 'management',')'] 
                en_sample = word_match[chunk_idx] + word_match[chunk_idx+1] # en_sample =  '(disaster'
                sso_idx = chunk_idx # word_match 안에서의 idx

                ##################### 영어 #######################
                # sent 안에서 en_sample와 일치하는 것을 찾아줄건데 index error 안나게 range(0, sent길이 - en_sample길이)
                for en_start in range(0, len(sent) - len(en_sample)):
                    # 탐색의 길이는 1 아니라 en_sample 전체의 길이만큼 이라서 sent[인덱스:인덱스+en_sample길이]
                    if sent[en_start:en_start+len(en_sample)] == en_sample:
                        # 정말 중요한 기준점 찾음!
                        btw_ko_en = en_start
                        # 첨부터 탐색해줄 필요 없음 btw_ko_en 인덱스부터 찾고 괄호 찾으면 멈추기
                        for en_end in range(btw_ko_en, len(sent)):
                            # 괄호 찾았니? 
                            if sent[en_end] == ssc:
                                # 괄호는 건너 뛰어야 하니까, btw_ko_en + 1 ~ en_end
                                en_word = sent[btw_ko_en+1:en_end]
                                break  
                 
        # print(f'sso_idx {sso_idx}')
        ##################### 한글 #######################
        ko_word = str()
        # list 안에서 괄호의 index가 1 이면 한글 단어는 한 덩어리만 있는걸로 인식. 그래서 바로 한글로 넣어주기
        if sso_idx == 1:
            # print(f'ko_word {ko_word}')
            ko_word = word_match[0]
        # 그게 아니라면 할일은 많아지지...
        else:
            # ko_start - 단어의 처음, ko_end는 괄호 앞에 있는 idx 까지
            ko_start, ko_end = word_match[0], word_match[sso_idx-1]
            len_ko_start , len_ko_end = len(ko_start), len(ko_end)
    
            ko_start_idx, ko_end_idx = 0, btw_ko_en 
            
            # 어디서부터 한글 탐색할지
            which_to_find_ko_index = 0
            
            if btw_ko_en <= 5:
                which_to_find_ko_index = 0
                # print('c1')
            else: 
                which_to_find_ko_index = btw_ko_en - 15
                # print('c2')
                if which_to_find_ko_index < 0:
                    which_to_find_ko_index = 0
                    # print('c3')
                    

            
            # 한글 첫번째 단어의 첫 index 찾기
            for find_ko_start_idx in range(which_to_find_ko_index, btw_ko_en):
               
                if sent[find_ko_start_idx:find_ko_start_idx+len_ko_start] == ko_start:
                    ko_start_idx = find_ko_start_idx
                    break

            # 한글 마지막 단어의 첫 index 찾기
            for find_ko_end_idx in range(ko_start_idx +1, btw_ko_en - len_ko_end + 1):
                if sent[find_ko_end_idx:find_ko_end_idx + len_ko_end] == ko_end:
                    ko_end_idx = find_ko_end_idx + len_ko_end
                    break
            
            # 한글의 첫번째 index라고 찾은 아이의 단어와, ko_word[0]가 같다면 진행하기
            if sent[ko_start_idx:ko_start_idx+len_ko_start] == ko_start:
                ko_word = sent[ko_start_idx:ko_end_idx]
            # 한글의 첫번째 index라고 찾은 아이의 단어와, ko_word[0]가 같지 않다면 다시 찾아서 진행하기
            else:
                for index in range(0, btw_ko_en):
                    if sent[index] == ko_start:
                        ko_word = sent[index:btw_ko_en+1]
                        break

        if skip_mored_word(en_word) == True or skip_dirty_words(en_word) == True:
            continue
        else:
            en_words_pre.append(en_word)  
            ko_words_pre.append(ko_word)

        # 중복되는 단어 제거  
        for ko_pre_idx in range(len(ko_words_pre)):   
            if ko_words_pre[ko_pre_idx] not in ko_words and en_words_pre[ko_pre_idx] not in en_words:
                if isKorean(ko_words_pre[ko_pre_idx]) == True:
                    if en_words_pre[ko_pre_idx][-1] in [' ', '(', ',']:
                        continue
                    ko_words.append(ko_words_pre[ko_pre_idx])
                    en_words.append(en_words_pre[ko_pre_idx])
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
    
    # 형태소 패턴 (list)와 일치하는 단어(list) 찾아서 추출
    word_match_list, mor_match_list = find_word(mor_match_list, words_list, morphemes_list)
    
	# Raw Sent에 대한 수술 후 뽑혀진 한-영 짝꿍들
    # ko_words, en_words = make_word_str(word_match_list, sent)
    
    # 띄어쓰기 이슈 해결하는 함수
    ko_words, en_words = find_good_korean_english(word_match_list, sent)

    return ko_words, en_words
