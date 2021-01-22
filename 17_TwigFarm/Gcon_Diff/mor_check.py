import nltk

from tensorflow.keras.preprocessing.text import text_to_word_sequence

# 마지막 인덱스인지 체크
def in_whether_last_idx(idx, words_list):
    length = len(words_list)
    if idx == length - 1:
        return True
    elif idx != length - 1:
        return False


# 형태소 분석 nltk tokenizer
def in_start_tokenizer(sent):
    # 단어만
    pre_words_list = text_to_word_sequence(sent) # [Hi, My, name, is, jihye]
    pre_words_list_1 = nltk.tokenize.word_tokenize(sent)[-1] # 마지막 마침표 ... 떨어뜨려주기
    if pre_words_list_1 in [',', '.', '!', '?']:
        pre_words_list.append(pre_words_list_1)
    
    words_list = list()
    for word in pre_words_list:
        pre = word.split(' ')
        for _ in pre:
            words_list.append(_)

    # 단어와 형태소 List
    words_mor_list = nltk.tag.pos_tag(words_list) # [(Hi, NNG), ...] 

    # 형태소만 
    mor_list = list()
    for each_mor in words_mor_list:
        mor_list.append(each_mor[1]) # [NNG, NNP, VB ...]

    return words_list, mor_list, words_mor_list


# 단어 바꿔주기 
def in_words_change(tp, idx, words_list, mor_list, words_mor_list):
    if tp == 'vbin':
        words_list[idx] = f'{words_mor_list[idx][0]} {words_mor_list[idx+1][0]}' # 동사 두개 이어줌!
        mor_list[idx] = f'{words_mor_list[idx][1]} {words_mor_list[idx+1][1]}' # 형태소 두개 이어줌!
        words_list.pop(idx+1) # 뒤에 단어는 삭제해주기
        mor_list.pop(idx+1) # 뒤에 형태소는 삭제해주기
    return words_list, mor_list


# 동사 전치사 이어주기 # [(Hi, NNG), ...] = [(단어, 형태소), ...]
def in_vb_in_connect(words_list, mor_list, words_mor_list):
    for idx, each_word_mor in enumerate(words_mor_list):
        if each_word_mor[1] == 'VB' or each_word_mor[1] == 'NN':
            if idx == len(words_mor_list) - 1: # 끝번호면 작업하면 index error
                continue
            else: # 앞에 관사('DT')가 없으면 명사('NN')로 인식해서 가져가시오
                if words_mor_list[idx-1][1] != 'DT' and words_mor_list[idx+1][1] == 'IN': 
                    tp = 'vbin'
                    words_list, mor_list = in_words_change(tp, idx, words_list, mor_list, words_mor_list)
                
    return words_list, mor_list