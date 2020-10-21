import MeCab
import re

# 형태소 분석
def start_mecab(sent):
    m = MeCab.Tagger()
    te = m.parse(sent)
    print(te)
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
    word_mor_dict = dict()
    key = ''
    value = ''
    words = list()
    words_str = str()
    morphemes = list()
    morphemes_str = str()

    for i in range(len(raw_mor)):
        # print(i+1)
        # 짝수
        if i % 2 == 0:
            key = raw_mor[i]
            # print(key)
            words.append(key)
            words_str += key
        # 홀수
        else: 
            value = raw_mor[i].split(',')
            value = value[0]
            # print(value)
            morphemes.append(value)
            morphemes_str += value
        
        word_mor_dict[key] = value
    
    return words, morphemes, morphemes_str, word_mor_dict

# 패턴찾아서 리스트에서 찾기
def find_mo_pattern(morphemes_str):
    mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    # mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)' #괄호 포함 하지 않음
    
    mor_match_pre = re.findall(mor_pattern, morphemes_str, flags=0)
    mor_match = list()
    # ''없애주기
    for i in range(len(mor_match_pre)):
        sample = [i for i in mor_match_pre[i] if len(i) >= 1 ]
        mor_match.append(sample)
    # print(mor_match)
    
    return mor_match


# 형태소 패턴과 일치하는 단어 찾아서 추출
def find_word(mor_match, morphemes, words):
    word_match = list()
    for mor_match_idx in range(len(mor_match)):
        # print(len(morphemes))
        # print(len(mor_match[mor_match_idx]))
        for i in range(0, len(morphemes)-len(mor_match[mor_match_idx])):
            comparison = [morphemes[j] for j in range(i, i+len(mor_match[mor_match_idx]))]
            # print(comparison)
            if comparison == mor_match[mor_match_idx]:
                # print(words[i:i+len(mor_match[mor_match_idx])])
                word_match.append(words[i:i+len(mor_match[mor_match_idx])])
    
    return word_match

   
def find_pattern_show_words(sent):
    # 형태소 분석
    sent = start_mecab(sent)

    # 단어, 품사 구별
    raw_mor = words_morph(sent)
    
    # 형태소 패턴과 일치하는 것 찾아서 추출
    words, morphemes, morphemes_str, word_mor_dict = words_mors(raw_mor)

    # 형태소 패턴찾아서 리스트에서 찾기
    mor_match = find_mo_pattern(morphemes_str)
    
    # 형태소 패턴과 일치하는 단어 찾아서 추출
    word_matched = find_word(mor_match, morphemes, words)

    return word_matched

def isKorean(single_word):
    ko = re.compile('[ㄱ-ㅣ가-힣]')
    return bool(ko.match(single_word))

def isEnglish(single_word):
    en = re.compile('[a-zA-Z]')
    return bool(en.match(single_word))


def make_str(word_matched):
    ko_words = list()
    en_words = list()
    for single_list in word_matched:
        # print(single_list)
        ko_word = str()
        en_word = str()
        for single_word in single_list:
            if isKorean(single_word) == True:
                ko_word += single_word
            elif isEnglish(single_word) == True:
                en_word += single_word + ' '
        ko_words.append(ko_word)
        en_words.append(en_word)
    print(ko_words, '-', en_words)
    return ko_words, en_words

