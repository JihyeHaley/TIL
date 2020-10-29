import MeCab
from konlpy.tag import Mecab
mecab = Mecab()
print(mecab.morphs(u'안녕하세요 지혜입니다.'))
print(mecab.pos(u'안녕하세요 지혜입니다.'))
sent = '빠 른 생리식염수 투여를(rapid fluid administration) 하였 다.'
# sent = f'u\'{sent}\'
# print(type(mecab.pos('u'+sent)[1]))


# 형태소 분석
def start_mecab(sent):
    m = MeCab.Tagger()
    te = m.parse(sent)
    return te
    # tagger = Mecab()
    # print(tagger.pos('혼성단체(hybrid  entity)혼성비대칭 거래(hybrid  mismatch  arrangements)구나 2018년 5월 베이징에서 열린 ISO/TC 184 연례회의(Super Meeting)에서는 스마트 제조가 주요 화제였다.'))


#  단어, 품사 구별 [짝수(단어), 품사[0](품사)]
def words_morph(sent):
    mecab = Mecab()
    # sent = 'u'+sent
    sent = mecab.pos('u'+sent)
    print(sent)
    # sent = re.sub(r'(\,\*)*(\n|\t)','\n', sent)
    # sent = sent.split('\n') ddd
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
    print(raw_mor)
    for i in range(len(raw_mor)):
        words_list.append(raw_mor[i][0])
        morphemes_list.append(raw_mor[i][1])
        morphemes_one_str += raw_mor[i][1]
        # print(i+1)
        # 짝수
        # if i % 2 == 0:
        #     key = raw_mor[i]
        #     # print(key)
        #     words_list.append(key)
        #     words_one_str += key
        # # 홀수
        # else: 
        #     # wecab으로 뽑아낸 형태소의 값 1개만 뽑아주기 위해서
        #     value = raw_mor[i].split(',')
        #     value = value[0]
        #     # print(value)
        #     morphemes_list.append(value)
        #     morphemes_one_str += value
        
        # word_mor_dict[key] = value


    return words_list, morphemes_list, morphemes_one_str


te = start_mecab(sent)


# 단어, 품사 구별 [짝수(단어), 품사[0](품사)
raw_mor = words_morph(sent)


# dict_list에 구별해서 단어, 형태소 각각 넣어주기
    # raw_mor 한 문장을 쪼개서 짝수 - 단어, 홀수 - 형태
    # 품사를 모두 모아서 String으로 만들어주기 (pattern을 잡기위해서)
words_list, morphemes_list, morphemes_one_str = split_words_collect_mors(raw_mor)
