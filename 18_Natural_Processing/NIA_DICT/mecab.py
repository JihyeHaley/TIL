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
    # print(te)
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
    mor_pattern = '(VV\+ETM)?(MM)?(XPN|XSV)?(ETN)?(NNG|NNP)?(XR)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN+JX)?(VX)?(ETN)?(NNB)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(JKG)?(NNG|NNP)?(VA+ETM)?(IO)?(NNG|NNP)(XSN|XSV|XSA)?(XSA+ETM)?(JKO)?(SSO)(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SY)?(SL)?(SL)?(SC)?(SL)?(SL)?(SN)?(SN)?(SC)?(SL)?(SC)?(SN)?(SL)?'#괄호 있어야만함 처음에만
    
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
    # print(f'word_match_list : {word_match_list}')
    return word_match_list, mor_match_list

def get_right_ko_word(ko_words, en_words, sent):
    ko_space_ko = list()
    for idx, ko_word in enumerate(ko_words):
        first_en = en_words[idx][:2]
        # 영어 
        en_scc_and_en = f'(\({first_en})'
        # 한글 (안\붙임)
        len_first_ko = len(ko_word)
        allMatch = re.findall(en_scc_and_en, sent)
        find_this_en = allMatch[0]
        scc_en = len(find_this_en)

        # (영어 를 찾아서 어디 index부터 작업할지 찾기
        find_ko_first_index = 0
        print(f'sent: {sent}')
        print(f'find_this_en: {len(find_this_en)}')
        for idx in range(0, len(sent) - scc_en):
            # print(f'sent[idx:idx+scc_en]: {sent[idx:idx+scc_en]}')
            if sent[idx:idx+scc_en] == find_this_en:
                find_ko_first_index = idx
                break

        # 어디서부터 한글 탐색할지
        which_to_find_ko_index = 0
        if find_ko_first_index == 0:
            which_to_find_ko_index = find_ko_first_index - (len_first_ko + 3)
            print(which_to_find_ko_index)
        else:
            which_to_find_ko_index = find_ko_first_index
        if which_to_find_ko_index < 5:
            which_to_find_ko_index = 0
        print(which_to_find_ko_index)


        # 한글의 첫 글자, 한글의 마지막 글자
        ko_first, ko_last = ko_word[0], ko_word[-1]


        # 한글의 첫 글자 인덱스 default, 한글의 마지막 글자 인덱스 default
        ko_first_idx, ko_last_idx = 0, 0

        # 한글 첫 글자 찾으면 count 해줄 변수 아이
        ko_first_cnt = 0
        for index in range(which_to_find_ko_index, len(sent)):
            for idx in range(0, len(sent)):
                if sent[idx] == ko_first:
                    ko_first_idx = idx
                    ko_first_cnt += 1
                    if ko_first_cnt == 1:
                        break 
        print(f'ko_first_idx: {ko_first_idx}')
        print(sent[ko_first_idx])
        ko_made_word = ''
        for index in range(ko_first_idx, len(sent)):
            if sent[index] == ko_last:
                ko_last_idx = index
                ko_made_word = sent[ko_first_idx:ko_last_idx+1]
                print(sent[ko_first_idx:ko_last_idx+1])
                ko_space_ko.append(ko_made_word)
                break
            
    return ko_space_ko



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

    ko_words = get_right_ko_word(ko_words, en_words, sent)

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

# 영어입니까?
def isNumber(single_word):
    en = re.compile('[0-9]')
    return bool(en.match(single_word))


# Fig 같이 필요 없는 덩어리 아예 없애기
def skip_dirty_words(single_word):
    if 'see Fig' in single_word  or 'Fig' in single_word or 'r . ' in single_word or 'Table' in single_word:
        return True
    else:
        return False



# 살릴 단어 만들기
def make_word_str(word_matched_list):
    ko_words = list()
    en_words = list()
    # 대문자
    for single_list in word_matched_list:
        # print(single_list)
        ko_word = str()
        en_word = str()
        
        check_start_en = 0
        for find_en_begin in single_list:
            if isEnglish(find_en_begin) == False:
                check_start_en += 1
            elif isEnglish(find_en_begin) == True:
                check_start_en += 1
                break
        for d_i in range(len(single_list)):
            if d_i < check_start_en - 1 :
                if single_list[d_i] in ['(', ')', '{', '}', '[', ']', 'Δ', '㈜)'] or single_list[d_i] in ['은', '는', '을', '를', '이', '가', '경우', '의한']:
                    continue
                ko_word += single_list[d_i]
            else:
                if single_list[d_i] in ['(', ')', '{', '}', '[', ']']:
                    continue
                en_word += single_list[d_i] + ' '
        ko_words.append(ko_word)
        en_words.append(en_word)
    # print(ko_words, '\n', en_words)
    print('#'*30)
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
    skip_word = ['Fig','fig', 'Fig.','fig.', 'a', 'aa', 'aaa', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vv', 'vii', 'viii', 'x', 'xx', 'ix', 'xi', 'xiv', 'xiii', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VV', 'VII', 'VIII', 'X', 'XX', 'IX', 'XIII']
    if len(mored_word) == 1 or mored_word in skip_word:
        return True
    else:
        return False
