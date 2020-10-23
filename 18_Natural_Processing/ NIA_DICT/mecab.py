import MeCab
import re

# 형태소 분석
def start_mecab(sent):
    m = MeCab.Tagger()
    te = m.parse(sent)
    return te
    # tagger = Mecab()
    # print(tagger.pos('혼성단체(hybrid  entity)혼성비대칭 거래(hybrid  mismatch  arrangements)구나 2018년 5월 베이징에서 열린 ISO/TC 184 연례회의(Super Meeting)에서는 스마트 제조가 주요 화제였다.'))




# 단어, 품사 구별
def words_morph(sent):
    sent = re.sub(r'(\,\*)*(\n|\t)','\n', sent)
    sent = sent.split('\n')
    
    return sent




# dict_list에 구별해서 단어, 형태소 각각 넣어주기
# raw_mor 한 문장을 쪼개서 짝수 - 단어, 홀수 - 형태소 
def words_mors(raw_mor):
    key = ''
    value = ''
    word_mor_dict = dict()
    words_list = list()
    words_one_str = str()
    morphemes_list = list()
    morphemes_one_str = str()

    for i in range(len(raw_mor)):
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
    return words_list, morphemes_list, words_one_str, morphemes_one_str




# 패턴찾아서 리스트에서 찾기
def find_mor_pattern(morphemes_one_str):
    # mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    # mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)' #괄호 있어야만함
    # mor_pattern = '(XPN|XSV)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    # mor_pattern = '(XPN|XSV)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)'#괄호 있어야만함
    mor_pattern = '(XPN|XSV)?(ETN)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(JX)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(NNG|NNP)?(XSN|XSV|XSA)?(JKO)?(SSO)(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SL)?'#괄호 있어야만함
    
    mor_match_pre = re.findall(mor_pattern, morphemes_one_str, flags=0)
    mor_match_list= list()
    # ''없애주기
    for i in range(len(mor_match_pre)):
        sample = [i for i in mor_match_pre[i] if len(i) >= 1 ]
        mor_match_list.append(sample)
    print('mor_match_list:', mor_match_list)
    return mor_match_list




# 형태소 패턴과 일치하는 단어 찾아서 추출
def find_word(mor_match_list, words_list, morphemes_list):
    word_match_list = list()
    for mor_match_idx in range(len(mor_match_list)):
        # print(len(morphemes))
        # print(len(mor_match[mor_match_idx]))
        for i in range(0, len(morphemes_list)-len(mor_match_list[mor_match_idx])):
            comparison = [morphemes_list[j] for j in range(i, i+len(mor_match_list[mor_match_idx]))]
            # print(comparison)
            if comparison == mor_match_list[mor_match_idx]:
                # print(words[i:i+len(mor_match[mor_match_idx])])
                word_match_list.append(words_list[i:i+len(mor_match_list[mor_match_idx])])
    
    print('word_match_list:', word_match_list)
    return word_match_list

   
def find_pattern_show_words(sent):
    # 형태소 분석
    te = start_mecab(sent)

    # 단어, 품사 구별
    raw_mor = words_morph(te)
    
    # 형태소 패턴과 일치하는 것 찾아서 추출
    words_list, morphemes_list, words_one_str, morphemes_one_str = words_mors(raw_mor)

    # 형태소 패턴찾아서 리스트에서 찾기
    mor_match_list = find_mor_pattern(morphemes_one_str)
    
    # 형태소 패턴과 일치하는 단어 찾아서 추출
    word_match_list = find_word(mor_match_list, words_list, morphemes_list)
    
    mor_match_list_str = list()

    for mm in word_match_list:
        mmp = ''
        for m in range(len(mm)):
            mmp += mm[m] + '-'
        mor_match_list_str.append(mmp)
    # print('mor_match_list_str: ', mor_match_list_str)

    return te, word_match_list, mor_match_list_str


def isKorean(single_word):
    ko = re.compile('[ㄱ-ㅣ가-힣]')
    return bool(ko.match(single_word))

def isEnglish(single_word):
    en = re.compile('[a-zA-Z]')
    return bool(en.match(single_word))


def make_str(word_matched_list):
    ko_words = list()
    en_words = list()
    for single_list in word_matched_list:
        # print(single_list)
        ko_word = str()
        en_word = str()
        for single_word in single_list:
            # 한글 만들어주기
            if isKorean(single_word) == True:
                ko_word += single_word
            # 영어 만들어주기
            elif isEnglish(single_word) == True:
                en_word += single_word + ' '
        ko_words.append(ko_word)
        en_words.append(en_word)
    # print(ko_words, '-', en_words)
    return ko_words, en_words

