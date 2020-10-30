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

ex = '빠 른 생리식염수 투여를(rapid fluid administration) 하였 다.'
ex = '객담에서의 항산균 도말 검사(acid-fast bacillus smear test)와 결핵균 중합효소연쇄 반응 검사도 모두 음성이었다. '
ex = '흉수의 아데노신탈아미노효소(ade- nosinedeaminase, ADA)는 127 U/L이었다. '
ex = '패혈증 치료를 위하여 항생제(piperacillin/tazobactam)와 다량의 수액을 투여하였다. '
ex = '후두마스크(laryngeal mask airway, LMA)는 응급 상황에서의 기도유지는 물론 전신마취시에 기관내삽관을 대신하여 많이 사용되고 있다.'
ex = '21세기 초반 브라질에서는 관광분야, 특히 호텔산업이 브라질의 환경과 사회에 미치는 부정적 영향에 대한 우려가 커졌다.ISO 21401을 개발한 작업반의 알렉산드르 가리도(Alexandre Garrido) 컨비너에 따르면, “ISO 21401은 브라질의 호텔 업계가 2006년 이래 도입해온 브라질 표준 ABNT NBR 15401을 모체로 개발되었다”고 한다.'

def words_morph(sent):
    sent = re.sub(r'(\,\*)*(\n|\t)','\n', sent)
    te = sent.split('\n')
    print(te)
    return te



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
            value = raw_mor[i].split(',')
            value = value[0]
            # print(value)
            morphemes_list.append(value)
            morphemes_one_str += value
        
        word_mor_dict[key] = value
    print(word_mor_dict)
    return words_list, morphemes_list, words_one_str, morphemes_one_str

# 패턴찾아서 리스트에서 찾기
def find_mor_pattern(morphemes_one_str):
    # mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    # mor_pattern = '(NNG|NNP)?(NNG|NNP)?(NNG|NNP)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)' #괄호 있어야만함
    # mor_pattern = '(XPN|XSV)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(SSO)?(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)?'
    # mor_pattern = '(XPN|XSV)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(NNG|NNP)?(XSN|XSV|XSA)?(SSO)(SL)(SY)?(SL)?(SY)?(SL)?(SY)?(SL)?(SSC)'#괄호 있어야만함
    mor_pattern = '(XPN|XSV)?(ETN)?(NNG|NNP)(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(JX)?(NNG|NNP)?(XSN|XSV|XSA)?(XPN|XSV)?(ETN)?(NNG|NNP)?(XSN|XSV|XSA)?(JKO)?(SSO)(SL)(SY)?(SC)?(SL)?(SY)?(SL)?(SY)?(SL)?(SL)?(SL)?(SC)?(SL)?'#괄호 있어야만함
    
    mor_match_pre = re.findall(mor_pattern, morphemes_one_str, flags=0)
    mor_match_list = list()
    # ''없애주기
    for i in range(len(mor_match_pre)):
        sample = [i for i in mor_match_pre[i] if len(i) >= 1 ]
        mor_match_list.append(sample)
    print(mor_match_list)
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
    print(word_match_list)
    return word_match_list


def find_pattern_show_words(sent):
    # 형태소 분석
    sent = start_mecab(sent)

    # 단어, 품사 구별
    raw_mor = words_morph(sent)
    
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
    print('mor_match_list_str: ', mor_match_list_str)
    print('word_match_list: ', word_match_list)
    return word_match_list, mor_match_list_str


# 한글인지
def isKorean(single_word):
    ko = re.compile('[ㄱ-ㅣ가-힣]')
    return bool(ko.match(single_word))

#영어인지
def isEnglish(single_word):
    en = re.compile('[a-zA-Z]')
    return bool(en.match(single_word))


def make_str(word_match_list):
    ko_words = list()
    en_words = list()
    for single_list in word_match_list:
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
    print('make_str(word_match_list): ',ko_words, '-', en_words)
    return ko_words, en_words


# ex = start_mecab(ex)
# ex = words_morph(ex)
words_list, morphemes_list, words_one_str, morphemes_one_str = words_mors(ex)
mor_match_list = find_mor_pattern(morphemes_one_str)
word_match_list = find_word(mor_match_list, words_list, morphemes_list)
word_match_list, mor_match_list_str = find_pattern_show_words(ex)
make_str(word_match_list)